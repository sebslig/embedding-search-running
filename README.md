# Semantic Search Query Engine

A distributed query engine for performing semantic search across multiple embedding databases. This project provides a foundational structure for federating queries, aggregating results, and presenting a unified search experience.

## Features

- **Distributed Querying**: Routes queries to multiple registered embedding databases.
- **Result Aggregation**: Combines and ranks search results from diverse sources.
- **Pluggable Databases**: Designed to support various embedding database backends.

## Getting Started

### Prerequisites

- Python 3.8+
- pip

### Installation

```bash
pip install -r requirements.txt
```

## Basic Usage (Conceptual)

```python
from engine.query_engine import QueryEngine
from databases.mock_database import MockEmbeddingDatabase

engine = QueryEngine()
engine.register_database(MockEmbeddingDatabase(name="DB1", embeddings=[[0.1,0.2],[0.3,0.4]]))
engine.register_database(MockEmbeddingDatabase(name="DB2", embeddings=[[0.5,0.6],[0.7,0.8]]))

query_vector = [0.2, 0.3]
results = engine.search(query_vector, k=2)

for result in results:
    print(f"Database: {result['db_name']}, Item: {result['item']}, Score: {result['score']}")
```

## Project Structure

- `engine/`: Core query engine logic.
- `databases/`: Interfaces and example implementations for embedding databases.
- `utils/`: Utility functions.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.