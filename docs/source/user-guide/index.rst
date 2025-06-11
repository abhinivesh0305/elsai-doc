User Guide
==========

Welcome to the Elsai Core User Guide. This section provides comprehensive documentation for all Elsai components and modules.

.. toctree::
   :hidden:
   :maxdepth: 2
   :caption: Elsai Core Components


   elsai-model
   elsai-text-extractors
   elsai-ocr-extractors
   elsai-prompts
   elsai-db
   elsai-cloud-connectors
   elsai-embeddings
   elsai-vectordb
   elsai-retrievers
   elsai-nli
   elsai-stt
   elsai-utilities

Components Overview
-------------------

**Large Language Models**

* :doc:`elsai-model <elsai-model>`: Connects to and manages LLMs from OpenAI, Azure OpenAI, and Amazon Bedrock.

**Document Processing**

* :doc:`elsai-text-extractors <elsai-text-extractors>`: Extracts raw text from structured documents like PDF, DOCX, CSV, and Excel.
* :doc:`elsai-ocr-extractors <elsai-ocr-extractors>`: Extracts text from scanned PDFs and images using OCR services like Azure, Textract, and Vision AI.
* :doc:`elsai-utilities <elsai-utilities>`: Provides tools for chunking and converting documents for use in retrieval pipelines.

**Data and Storage**

* :doc:`elsai-db <elsai-db>`: Executes natural language queries over SQL databases using LLM-powered connectors.
* :doc:`elsai-embeddings <elsai-embeddings>`: Generates vector embeddings from text using Azure OpenAI embedding models.
* :doc:`elsai-vectordb <elsai-vectordb>`: Stores and retrieves document embeddings using ChromaDB or Pinecone for semantic search.
* :doc:`elsai-cloud-connectors <elsai-cloud-connectors>`: Enables file operations across cloud platforms like AWS S3, Azure Blob, SharePoint, and OneDrive.

**Retrieval and Search**

* :doc:`elsai-retrievers <elsai-retrievers>`: Combines semantic and keyword-based retrieval to enhance document search accuracy.
* :doc:`elsai-nli <elsai-nli>`: Lets users query structured data like CSV files using natural language and LLMs.

**Audio and Prompts**

* :doc:`elsai-stt <elsai-stt>`: Transcribes audio files to text using Azure's hosted Whisper model.
* :doc:`elsai-prompts <elsai-prompts>`: Retrieves and manages prompt templates from Pezzo for version-controlled prompt engineering.

Getting Started
---------------

To get started with Elsai Core, we recommend beginning with :doc:`elsai-model <elsai-model>` to understand how to connect to and manage language models, which forms the foundation for most other components.