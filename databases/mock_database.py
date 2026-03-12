import numpy as np
from databases.embedding_database import EmbeddingDatabase

class MockEmbeddingDatabase(EmbeddingDatabase):
    def __init__(self, name: str, embeddings: list = None, items: list = None):
        super().__init__(name)
        self.embeddings = np.array(embeddings) if embeddings is not None else np.array([])
        self.items = items if items is not None else [f"item_{i}" for i in range(len(self.embeddings))]

        if len(self.embeddings) != len(self.items):
            raise ValueError("Number of embeddings must match number of items")

        print(f"Mock database '{self.name}' initialized with {len(self.embeddings)} embeddings.")

    def search(self, query_vector: list, k: int) -> list:
        if len(self.embeddings) == 0:
            return []

        query_vec = np.array(query_vector)
        
        # Calculate cosine similarity (or can be Euclidean distance)
        # Normalizing vectors first for dot product to be cosine similarity
        norm_query_vec = query_vec / np.linalg.norm(query_vec)
        norm_embeddings = self.embeddings / np.linalg.norm(self.embeddings, axis=1, keepdims=True)
        
        similarities = np.dot(norm_embeddings, norm_query_vec)

        # Get top k indices
        top_k_indices = np.argsort(similarities)[::-1][:k]

        results = []
        for idx in top_k_indices:
            results.append({
                'item': self.items[idx],
                'score': float(similarities[idx]),
                'db_name': self.name
            })
        return results
