Elsai VectorDB
==============

The **Elsai VectorDB** package provides interfaces to work with vector databases like **ChromaDB** and **Pinecone**, enabling efficient storage and retrieval of document embeddings.

Prerequisites
-------------

- Python 3.13
- `.env` file with appropriate API keys and configuration variables

Installation
------------

To install the `elsai-vectordb` package:

.. code-block:: bash

   pip install --index-url https://elsai-core-package.optisolbusiness.com/root/elsai-vectordb/ elsai-vectordb==0.1.0

Components
----------

1. ChromaVectorDb
~~~~~~~~~~~~~~~~~

`ChromaVectorDb` is a wrapper around ChromaDB to manage local document embeddings with persistent storage.

.. code-block:: python

   from elsai_vectordb.chromadb import ChromaVectorDb

   chroma_client = ChromaVectorDb(persist_directory="your_persist_directory") # Or set in environment variable CHROMA_PERSIST_DIRECTORY
   
   chroma_client.create_if_not_exists(collection_name="your_collection_name")

   document = {
       "id": "001",
       "embeddings": [0.1, 0.2, 0.7],  # Example embedding vector
       "page_content": "This is a sample document.",
       "metadatas": {"source": "example_source", "file_id": "doc1"}
   }

   chroma_client.add_document(document=document, collection_name="your_collection_name")

   documents = chroma_client.retrieve_document(
       collection_name="your_collection_name",
       embeddings=[0.1, 0.2, 0.7],
       files_id=["doc1"],
       k=5
   )

   collection = chroma_client.get_collection(collection_name="your_collection_name")

   chunks = chroma_client.fetch_chunks(collection_name="your_collection_name", files_id=["doc1"])

   chroma_client.delete_collection(collection_name="your_collection_name")

**Required Environment Variables:**

- ``CHROMA_PERSIST_DIRECTORY`` – Path to the directory where ChromaDB will persist data locally


2. PineconeVectorDb
~~~~~~~~~~~~~~~~~~~

`PineconeVectorDb` integrates with Pinecone to manage vector search using cloud-hosted infrastructure.

.. code-block:: python

   from elsai_vectordb.pinecone import PineconeVectorDb

   pinecone_client = PineconeVectorDb(
       index_name="testingindex",
       pinecone_api_key="pinecone_api_key",  # Or set in environment variable PINECONE_API_KEY
       dimension=1536  # Example dimension size
   )

   pinecone_client.add_document(
       document={
           "id": "001",
           "embeddings": [0.1, 0.2, 0.7],  # Replace with a 1536-dimension vector
           "page_content": "This is a sample document.",
           "metadatas": {"source": "example_source", "file_id": "doc1"}
       },
       namespace="namespacename"
   )

   results = pinecone_client.retrieve_document(
       namespace="namespacename",
       question_embedding=[0.1, 0.2, 0.7],
       files_id=["doc1"],
       k=5
   )

**Required Environment Variables:**

- ``PINECONE_API_KEY`` – API key to authenticate with Pinecone vector DB