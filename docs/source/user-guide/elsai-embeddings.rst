Elsai Embeddings
================

The **Elsai Embeddings** module enables seamless embedding generation using Azure OpenAI models.

Prerequisites
-------------

- Python 3.13
- `.env` file with appropriate API keys and configuration variables

Installation
------------

To install the `elsai-embeddings` package:

.. code-block:: bash

   pip install --index-url https://elsai-core-package.optisolbusiness.com/root/elsai-embeddings/ elsai-embeddings==0.1.0

Components
----------

1. Azure Embeddings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`AzureOpenAIEmbeddingModel` is a class that connects to the Azure OpenAI embedding service to generate vector representations of text queries and documents.

.. code-block:: python

   from elsai_embeddings.azure_embeddings import AzureOpenAIEmbeddingModel

   embeddings = AzureOpenAIEmbeddingModel(
       model="your_model_name",
       azure_api_key="your_azure_api_key",
       azure_api_version="your_azure_api_version",
       azure_deployment="your_azure_deployment_name",
       azure_endpoint="your_azure_endpoint"
   )  # Or set in environment variables AZURE_OPENAI_API_KEY, AZURE_OPENAI_ENDPOINT, OPENAI_API_VERSION, AZURE_EMBEDDING_DEPLOYMENT_NAME

   embed_text = embeddings.embed_query("Your text to embed")

   embed_docs = embeddings.embed_documents(["Document 1 text", "Document 2 text"])

**Required Environment Variables:**

- ``AZURE_OPENAI_API_KEY`` – API key for accessing the Azure OpenAI service.
- ``AZURE_OPENAI_ENDPOINT`` – Endpoint URL of your Azure OpenAI resource.
- ``OPENAI_API_VERSION`` – API version used for the embedding requests.
- ``AZURE_EMBEDDING_DEPLOYMENT_NAME`` – Deployment name for the embedding model on Azure.