.. elsai-docs documentation master file, created by
   sphinx-quickstart on Mon Jun  9 10:04:21 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. toctree::
   :hidden:
   :maxdepth: 1
   :caption: Contents

   user-guide/index

Elsai Core
==========

**Elsai Core** a modular framework that includes a rich set of components such as LLM connectors, extractors, prompts, vector databases, retrievers, NLI, STT, and document processing tools. These components can be combined to build powerful agents and language-driven applications with ease and flexibility.

Overview
--------

**Elsai Core** simplifies the development of intelligent, agent-based applications by offering a flexible set of modular components:

- **Modular Composition**: Build applications faster using ready-to-use modules such as file extractors (PDF, DOCX, CSV), model connectors (OpenAI, Azure, Bedrock), and chunkers — all designed to work seamlessly together.
- **Unified Orchestration**: Easily orchestrate full data-to-response pipelines with support for both structured (SQL, CSV) and unstructured (PDF, audio, DOCX) data using natural language interfaces.
- **Cloud-Ready Integration**: Connect to cloud services like **AWS S3**, **Azure Blob**, **SharePoint**, **Pinecone**, and **ChromaDB** with environment-based configurations and secure token management.
- **Hybrid Retrieval**: Enhance information relevance using Elsai's hybrid retrievers that combine dense (semantic) and sparse (keyword/BM25) search strategies.
- **Multimodal Input Support**: Handle not just text but also audio via Whisper, scanned PDFs via OCR, and spreadsheet data — all processed under a unified chunking and retrieval strategy.

Whether you're building autonomous agents, internal tools, or data-aware assistants, **Elsai Core** provides the foundation to move from prototype to production with reusable components and consistent design.

Architecture
------------

The Elsai Core ecosystem is composed of loosely coupled packages that work together seamlessly. Each component serves a specific purpose while maintaining compatibility with the broader ecosystem.


To learn more about each component and how to use them, visit the :doc:`User Guide <user-guide/index>` where you'll find detailed documentation for all Elsai modules.