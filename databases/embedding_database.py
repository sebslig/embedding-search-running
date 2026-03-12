from abc import ABC, abstractmethod

class EmbeddingDatabase(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def search(self, query_vector: list, k: int) -> list:
        """
        Performs a semantic search on the database.
        Returns a list of dicts, each with 'item', 'score', and 'db_name'.
        """
        pass
