Elsai Utilities
===============

The **Elsai Utilities** package provides helper classes for chunking and converting documents for use in retrieval-augmented generation (RAG) and vector database ingestion pipelines.

Prerequisites
-------------

- Python 3.13

Installation
------------

To install the `elsai-utilities` package:

.. code-block:: bash

   pip install --index-url https://elsai-core-package.optisolbusiness.com/root/elsai-utilities/ elsai-utilities==0.1.0

Components
----------

1. DocumentChunker
~~~~~~~~~~~~~~~~~~

The `DocumentChunker` class provides various ways to split text into structured chunks.

.. code-block:: python

   from elsai_utilities.splitters import DocumentChunker

   chunker = DocumentChunker()

   contents = "# This is the first page.\n\n## This is the second page.\n\n### This is the third page."

   # Page-wise chunking
   chunks = chunker.chunk_page_wise(contents=contents, file_name="example.md")
 

   # Markdown header-wise chunking
   markdown_wise_chunks = chunker.chunk_markdown_header_wise(
       text=contents,
       file_name="example.md",
       headers_to_split_on=[("#", "Header 1"), ("##", "Header 2")],
       strip_headers=True
   )


   # Recursive character-wise chunking
   text = "This is a long piece of text that should be chunked recursively..."
   recursive_chunks = chunker.chunk_recursive(
       contents=text,
       file_name="example.md",
       chunk_size=50,
       chunk_overlap=10
   )


2. DocumentConverter
~~~~~~~~~~~~~~~~~~~~

The `DocumentConverter` class converts LlamaIndex documents into LangChain-compatible `Document` objects.

.. code-block:: python

   from elsai_utilities.converters import DocumentConverter

   converter = DocumentConverter()

   llama_index_document = {
       "text_resource": {
           "text": "This is a sample text extracted from LlamaIndex."
       }
   }

   langchain_document = converter.llama_index_to_langchain_document(
       llama_index_document=llama_index_document,
       file_name="example.md"
   )




