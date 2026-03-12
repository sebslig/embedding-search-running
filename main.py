from engine.query_engine import QueryEngine
from databases.mock_database import MockEmbeddingDatabase
import numpy as np

def main():
    print("Initializing distributed semantic search engine...")
    engine = QueryEngine()

    # Register mock databases
    db1_embeddings = np.random.rand(5, 10).tolist() # 5 items, 10-dim embeddings
    db1_items = [f"product_{i}" for i in range(5)]
    engine.register_database(MockEmbeddingDatabase(name="ProductsDB", embeddings=db1_embeddings, items=db1_items))

    db2_embeddings = np.random.rand(4, 10).tolist() # 4 items, 10-dim embeddings
    db2_items = [f"document_{i}" for i in range(4)]
    engine.register_database(MockEmbeddingDatabase(name="DocumentsDB", embeddings=db2_embeddings, items=db2_items))

    # Simulate a query vector
    query_vector = np.random.rand(10).tolist()
    print(f"\nPerforming search with query vector: {query_vector[:3]}...")

    # Perform search
    top_k_results = engine.search(query_vector, k=3)

    print("\n--- Search Results ---")
    if not top_k_results:
        print("No results found.")
    for i, result in enumerate(top_k_results):
        print(f"Rank {i+1}: DB='{result['db_name']}', Item='{result['item']}', Score={result['score']:.4f}")

if __name__ == "__main__":
    main()
