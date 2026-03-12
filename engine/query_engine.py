import numpy as np
from concurrent.futures import ThreadPoolExecutor

class QueryEngine:
    def __init__(self):
        self.databases = {}
        self.executor = ThreadPoolExecutor(max_workers=5)

    def register_database(self, db_instance):
        self.databases[db_instance.name] = db_instance
        print(f"Registered database: {db_instance.name}")

    def _search_in_db(self, db_name, query_vector, k):
        db = self.databases[db_name]
        print(f"Querying database: {db_name}")
        return db.search(query_vector, k)

    def search(self, query_vector, k=5):
        if not self.databases:
            return []

        futures = [
            self.executor.submit(self._search_in_db, db_name, query_vector, k)
            for db_name in self.databases
        ]

        all_results = []
        for future in futures:
            all_results.extend(future.result())

        # Simple aggregation: sort all results by score (descending) and take top k
        all_results.sort(key=lambda x: x['score'], reverse=True)
        return all_results[:k]
