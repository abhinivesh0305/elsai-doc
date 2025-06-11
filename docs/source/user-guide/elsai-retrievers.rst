Elsai Retrievers
================

The **Elsai Retrievers** package provides an interface for performing **hybrid document retrieval** by combining **semantic** and **sparse (BM25)** search strategies. This enables more accurate and flexible information retrieval across multiple sources.

Prerequisites
-------------

- Python 3.13
- `.env` file with appropriate API keys and configuration variables

Installation
------------

To install the `elsai-retrievers` package:

.. code-block:: bash

   pip install --index-url https://elsai-core-package.optisolbusiness.com/root/elsai-retrievers/ elsai-retrievers==0.1.0

Component
---------

1. HybridRetriever
~~~~~~~~~~~~~~~~~~

`HybridRetriever` is a class that enables combining results from multiple retrievers — including dense vector-based (semantic) and sparse (BM25) — into a single ranked list.

.. code-block:: python

   from elsai_retrievers.hybrid_retriever import HybridRetriever

   # Create the hybrid retriever instance
   hybrid_retriever = HybridRetriever()

   # Perform hybrid retrieval
   results = hybrid_retriever.hybrid_retrieve(
       chunks=chunks,  # Optional: for BM25-based retrieval
       retrievers=["retriever1", "retriever2"],  # Semantic retrievers that support `.retrieve()`
       question="How does hybrid retrieval work?"
   )