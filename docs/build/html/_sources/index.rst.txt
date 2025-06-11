.. elsai-docs documentation master file, created by
   sphinx-quickstart on Mon Jun  9 10:04:21 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Elsai Core Documentation
========================

Welcome to the official documentation for the **Elsai Core** framework, a modular and extensible system designed to enable seamless **retrieval-augmented generation (RAG)** workflows across multiple data formats, cloud services, and model providers.

Elsai empowers developers and enterprises to build intelligent, language-driven applications with plug-and-play support for:

- Natural language querying over structured and unstructured data
- Document processing and chunking
- Cloud storage and webhook integrations
- Embedding generation and vector database operations
- Hybrid retrievers (semantic + keyword-based)
- Speech-to-text transcription using Whisper
- Prompt versioning and model orchestration

Each module in the Elsai Core ecosystem is independently installable and follows a consistent interface design to make integration simple and flexible.

This documentation provides detailed guidance on:

- Installation and setup
- Environment variables and credentials
- Python API usage with examples
- Supported backends and file formats

.. note::

   Make sure you are using **Python 3.13** and have a properly configured `.env` file for any component that requires API authentication.

Start exploring the components below to get the most out of **Elsai Core**.


Elsai Model
===========

The **Elsai Model** Package provides a unified interface to connect with three major LLM providers:

- OpenAI Connector
- Azure OpenAI Connector
- Bedrock Connector

Prerequisites
-------------

- Python 3.13
- `.env` file with appropriate API keys and configuration variables

Installation
------------

To install the `elsai-model` package:

.. code-block:: bash
  
   pip install --index-url https://elsai-core-package.optisolbusiness.com/root/elsai-model/ elsai-model==0.1.0



Components
----------

1. OpenAIConnector
~~~~~~~~~~~~~~~~~~

`OpenAIConnector` is a class designed to establish secure connections with the OpenAI API. It retrieves API credentials from environment variables and provides a method to initialize the connection with a specified language model.

.. code-block:: python

   from elsai_model.openai import OpenAIConnector

   connector = OpenAIConnector(openai_key="openai_key")  # Or set it as an environment variable
   model = connector.connect_open_ai(modelname="modelname")

**Required Environment Variable**:

- ``OPENAI_API_KEY`` – Your secret API key from OpenAI used to authenticate and authorize API requests.

2. AzureOpenAIConnector
~~~~~~~~~~~~~~~~~~~~~~~

`AzureOpenAIConnector` is a class that facilitates connecting to the Azure-hosted OpenAI service. It allows configuration through direct parameters or environment variables, and supports deployment-specific model initialization.

.. code-block:: python

   from elsai_model.azure_openai import AzureOpenAIConnector
   connector = AzureOpenAIConnector(
       azure_endpoint="https://your-azure-openai-endpoint.openai.azure.com/",
       openai_api_key="your-azure-openai-api-key",
       openai_api_version="2023-05-15",
       temperature=0
   )  # Or set it as an environment variable

   model = connector.connect_azure_open_ai(deploymentname="gpt-4o-mini")

**Required Environment Variables:**

- ``AZURE_OPENAI_API_KEY`` – API key used to authenticate with the Azure-hosted OpenAI service.
- ``AZURE_OPENAI_ENDPOINT`` – Endpoint URL of your Azure OpenAI resource.
- ``OPENAI_API_VERSION`` – API version to use when connecting to Azure OpenAI (e.g., 2023-05-15).
- ``AZURE_OPENAI_TEMPERATURE`` – Temperature value to control the randomness of model outputs (e.g., 0.0 for deterministic results).


3. BedrockConnector
~~~~~~~~~~~~~~~~~~~

`BedrockConnector` is a class for interacting with Amazon Bedrock, enabling secure LLM access via AWS credentials. It supports initialization with parameters or environment variables and allows model-specific connection.

.. code-block:: python

   from elsai_model.bedrock import BedrockConnector

   bedrockconnector = BedrockConnector(
       aws_access_key="your access key",
       aws_secret_key="your secret key",
       aws_session_token="your session token",
       aws_region="us-east-1",
       temperature=0.1
   )  # Or set it as an environment variable

   llm = bedrockconnector.connect_bedrock(model_id="amazon.titan-text-express-v1")

**Required Environment Variables:**

- ``AWS_ACCESS_KEY_ID`` – Your AWS access key ID for authenticating with AWS services.
- ``AWS_SECRET_ACCESS_KEY`` – Your AWS secret access key for secure authentication.
- ``AWS_SESSION_TOKEN`` – Temporary session token for secure AWS authentication (used with IAM roles or temporary credentials).
- ``AWS_REGION`` – AWS region (e.g., us-east-1) where the Bedrock service is hosted.
- ``BEDROCK_TEMPERATURE`` – Controls the randomness of the output from the model (optional; default can be set in code).


Elsai Text Extractors
=====================

The **Elsai Text Extractors** package provides utilities to extract structured or unstructured text data from various document formats. It supports:

- CSV files
- DOCX files
- PDF documents
- Excel spreadsheets

Prerequisites
-------------

- Python 3.13

Installation
------------

To install the `elsai-text-extractors` package:

.. code-block:: bash

   pip install --index-url https://elsai-core-package.optisolbusiness.com/root/elsai-text-extractors/ elsai-text-extractors==0.1.0

Components
----------

1. CSVFileExtractor
~~~~~~~~~~~~~~~~~~~

`CSVFileExtractor` reads and parses CSV files from the provided file path.

.. code-block:: python

   from elsai_text_extractors.csv_extractor import CSVFileExtractor

   extractor = CSVFileExtractor(file_path="sample_data/sample.csv")
   content = extractor.load_from_csv()

2. DocxTextExtractor
~~~~~~~~~~~~~~~~~~~~

`DocxTextExtractor` extracts plain text from Microsoft Word (.docx) documents.

.. code-block:: python

   from elsai_text_extractors.docx_extractor import DocxTextExtractor

   extractor = DocxTextExtractor(file_path="sample_data/sample.docx")
   content = extractor.extract_text_from_docx()

3. PyPDFTextExtractor
~~~~~~~~~~~~~~~~~~~~~

`PyPDFTextExtractor` extracts text from PDF documents using the PyPDF library.

.. code-block:: python

   from elsai_text_extractors.pypdfloader import PyPDFTextExtractor

   extractor = PyPDFTextExtractor(file_path="sample_data/sample.pdf")
   content = extractor.extract_text_from_pdf()

4. UnstructuredExcelLoader
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`UnstructuredExcelLoaderService` loads and parses Excel spreadsheets (.xlsx), handling unstructured formats gracefully.

.. code-block:: python

   from elsai_text_extractors.unstructured_excel_loader import UnstructuredExcelLoaderService

   extractor = UnstructuredExcelLoaderService(file_path="sample_data/sample.xlsx")
   content = extractor.load_excel()


Elsai OCR Extractors
=====================

The **Elsai OCR Extractors** package offers seamless integration with OCR services for extracting text from PDF documents. It currently supports:

- Azure Cognitive Service
- Azure Document Intelligence
- Llama Parse
- OpenAI VisionAI
- Amazon Textract

Prerequisites
-------------

- Python 3.13
- `.env` file with appropriate API keys and configuration variables

Installation
------------

To install the `elsai-ocr-extractors` package:

.. code-block:: bash

   pip install --index-url https://elsai-core-package.optisolbusiness.com/root/elsai-ocr-extractors/ elsai-ocr-extractors==0.1.0

Components
----------

1. AzureCognitiveService
~~~~~~~~~~~~~~~~~~~~~~~~

`AzureCognitiveService` is a class for extracting text from PDFs using Azure's Cognitive Services. It supports both direct initialization and environment variable-based configuration.

.. code-block:: python

   from elsai_ocr_extractors.azure_cognitive_service import AzureCognitiveService

   azure_ocr = AzureCognitiveService(
       file_path="your-file-path-here",
       subscription_key="your-subscription-key-here",
       endpoint="your-endpoint-here"
   )  # Or set it as an environment variable

   extracted_text = azure_ocr.extract_text_from_pdf()

**Required Environment Variables:**

- ``AZURE_SUBSCRIPTION_KEY`` – Your Azure OCR subscription key  
- ``AZURE_ENDPOINT`` – Your Azure OCR endpoint

2. AzureDocumentIntelligence
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`AzureDocumentIntelligence` is a class that utilizes Azure's advanced Document Intelligence to extract structured text from documents like PDFs.

.. code-block:: python

   from elsai_ocr_extractors.azure_document_intelligence import AzureDocumentIntelligence

   azure_ocr = AzureDocumentIntelligence(
       file_path="your-file-path",
       vision_endpoint="your-vision-endpoint",
       vision_key="your-vision-key"
   )  # Or set it as an environment variable

   extracted_text = azure_ocr.extract_text_from_pdf()

**Required Environment Variables:**

- ``VISION_ENDPOINT`` – Endpoint for Azure Document Intelligence  
- ``VISION_KEY`` – Subscription key for Azure Document Intelligence

3. Llama Parse Extractor
~~~~~~~~~~~~~~~~~~~~~~~~

`LlamaParseExtractor` is a wrapper class for interacting with the LlamaParse API to parse and load CSV data.

.. code-block:: python

   from elsai_ocr_extractors.llama_parse_extractor import LlamaParseExtractor

   llama_parse_extractor = LlamaParseExtractor(api_key="llama_parse_api_key")
   loaded_data = llama_parse_extractor.load_csv("path/to/your/file.csv")

4. VisionAI Extractor
~~~~~~~~~~~~~~~~~~~~~

`VisionAIExtractor` uses OpenAI's Vision AI to extract text from PDFs by converting pages to images and processing them using a language model.

.. code-block:: python

   from elsai_ocr_extractors.visionai_extractor import VisionAIExtractor

   extractor = VisionAIExtractor(api_key="openai_key", model_name="gpt-4o")  # Or set API key in env
   documents = extractor.extract_text_from_pdf(pdf_path="path_to_pdf.pdf")

**Required Environment Variable:**

- ``OPENAI_API_KEY`` – Your secret API key from OpenAI used to authenticate and authorize API requests.


5. Amazon Textract
~~~~~~~~~~~~~~~~~~

`AwsTextractConnector` interfaces with AWS Textract to extract text from PDFs. It supports multiple modes of operation including async document processing.

.. code-block:: python

   from elsai_ocr_extractors.awstextract import AwsTextractConnector

   textract_connector = AwsTextractConnector(
       access_key="aws_access_key",
       secret_key="aws_secret_key", 
       session_token="aws_session_token",
       region_name="aws_region", 
   )  # Or set environment variables

   # Extract text from local PDF
   documents = textract_connector.extract_text(file_path="path_to_pdf.pdf", s3_bucket="your_s3_bucket_name", s3_folder="your_s3_folder_name (OPTIONAL)")

   # Extract text from S3
   documents = textract_connector.extract_text_from_S3(s3_url="s3://bucket_name/folder_name/file.pdf")

   # Extract text with features
   documents = textract_connector.extract_text_features_from_S3(
       s3_url="s3://bucket_name/folder_name/file.pdf",
       features=["TABLES", "FORMS", "TEXT"]
   )

   # Asynchronous processing
   documents = textract_connector.async_process_document(
       s3_url="s3://bucket_name/folder_name/file.pdf",
       feature_list=["tables", "forms"]
   )

**Required Environment Variables:**

- ``AWS_ACCESS_KEY_ID`` – Your AWS access key ID used to authenticate API requests.  
- ``AWS_SECRET_ACCESS_KEY`` – Your AWS secret key paired with the access key for secure authentication.  
- ``AWS_SESSION_TOKEN`` – Temporary session token for using AWS STS or temporary credentials.  
- ``AWS_REGION`` – The AWS region where your resources (e.g., S3 bucket) are located.  
- ``S3_BUCKET`` – The name of your S3 bucket used for file uploads/downloads (REQUIRED ONLY FOR extract_text()).  
- ``S3_FOLDER`` – The folder path inside the S3 bucket for organizing files. (REQUIRED ONLY FOR extract_text()).  


Elsai Prompts
=============

The **Elsai Prompts** Package provides an interface to connect with the **Pezzo Prompt API**, allowing users to retrieve and manage project-specific prompts efficiently.

Prerequisites
-------------

- Python 3.13
- `.env` file with appropriate API keys and configuration variables

Installation
------------

To install the `elsai-prompts` package:

.. code-block:: bash

   pip install --index-url https://elsai-core-package.optisolbusiness.com/root/elsai-prompts/ elsai-prompts==0.1.0

Component
---------

1. PezzoPromptRenderer
~~~~~~~~~~~~~~~~~~~~~~

`PezzoPromptRenderer` is a class designed to fetch and retrieve prompts from the Pezzo API, enabling seamless access to project-specific prompts using either direct initialization or environment variables.

.. code-block:: python

   from elsai_prompts.pezzo import PezzoPromptRenderer

   pezzo = PezzoPromptRenderer(
       api_key="pezzo_api_key",
       project_id="project_id",
       environment="project_environment",
       server_url="server_url"
   )  # Set as environment variables or pass directly

   pezzo_prompts = pezzo.get_prompt("Prompt_Name")

**Required Environment Variables:**

- ``PEZZO_API_KEY`` – API Key for authenticating with the Pezzo API  
- ``PEZZO_PROJECT_ID`` – Identifier for the Pezzo project  
- ``PEZZO_ENVIRONMENT`` – Environment name (e.g., dev, prod)  
- ``PEZZO_SERVER_URL`` – Pezzo server base URL


Elsai DB Connectors
===================

The **Elsai DB** package provides connectors to interact with various SQL databases such as **MySQL**, **PostgreSQL**, and **ODBC** variants using natural language queries powered by an LLM.

Prerequisites
-------------

- Python 3.13
- `.env` file with appropriate API keys and configuration variables

Installation
------------

To install the `elsai-db` package:

.. code-block:: bash

   pip install --index-url https://elsai-core-package.optisolbusiness.com/root/elsai-db/ elsai-db==0.1.0




Components
----------

Required Environment Variables
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- ``DB_NAME`` – Name of the database
- ``DB_URL`` – Hostname or connection string of the database
- ``DB_USER`` – Username for database login
- ``DB_PASSWORD`` – Password for database login
- ``DB_DRIVER_NAME`` – ODBC driver name (only for ODBC connectors)

1. MySQLSQLConnector
~~~~~~~~~~~~~~~~~~~~

`MySQLSQLConnector` connects to a MySQL database using standard credentials and executes LLM-based queries.

.. code-block:: python

   from elsai_db.mysql import MySQLSQLConnector

   mysql_connector = MySQLSQLConnector(llm="llm-model", 
                                       database_name="your_database_name",
                                       database_password="your_database_password",
                                       database_user="your_database_user", 
                                       database_url="your_database_url")  # Or use env vars: DB_NAME, DB_URL, DB_USER, DB_PASSWORD

   result = mysql_connector.invoke("what are the names of all employees in the company?")


2. PostgreSQLConnector
~~~~~~~~~~~~~~~~~~~~~~

`PostgreSQLConnector` connects to a PostgreSQL database using standard credentials.

.. code-block:: python

   from elsai_db.postgres import PostgreSQLConnector

   postgres_connector = PostgreSQLConnector(llm="llm-model", 
                                            database_name="your_database_name",
                                            database_password="your_database_password",
                                            database_user="your_database_user", 
                                            database_url="your_database_url")  # Or use env vars: DB_NAME, DB_URL, DB_USER, DB_PASSWORD

   result = postgres_connector.invoke("what are the names of all employees in the company?")


3. OdbcMysqlConnector
~~~~~~~~~~~~~~~~~~~~~

`OdbcMysqlConnector` connects to MySQL via ODBC, which is useful for Windows environments or custom drivers.

.. code-block:: python

   from elsai_db.odbc_mysql import OdbcMysqlConnector

   odbc_mysql_connector = OdbcMysqlConnector(llm="llm-model",
                                             database_name="your_database_name",
                                             database_password="your_database_password",
                                             database_user="your_database_user", 
                                             database_url="your_database_url",
                                             driver_name="your_odbc_driver_name")  # Or use env vars: DB_NAME, DB_URL, DB_USER, DB_PASSWORD, DB_DRIVER_NAME

   result = odbc_mysql_connector.invoke("what are the names of all employees in the company?")


4. OdbcPostgresqlConnector
~~~~~~~~~~~~~~~~~~~~~~~~~~

`OdbcPostgresqlConnector` connects to PostgreSQL using ODBC drivers.

.. code-block:: python

   from elsai_db.odbc_postgres import OdbcPostgresqlConnector

   odbc_postgres_connector = OdbcPostgresqlConnector(llm="llm-model",
                                                     database_name="your_database_name",
                                                     database_password="your_database_password",
                                                     database_user="your_database_user", 
                                                     database_url="your_database_url",
                                                     driver_name="your_odbc_driver_name")  # Or use env vars: DB_NAME, DB_URL, DB_USER, DB_PASSWORD, DB_DRIVER_NAME

   result = odbc_postgres_connector.invoke("what are the names of all employees in the company?")




Elsai Cloud Connectors
=======================

The **Elsai Cloud Connectors** package provides utilities to interact with various cloud storage and notification services. It currently supports:

- AWS S3
- Azure Blob Storage
- Microsoft Graph Webhooks
- Microsoft OneDrive
- Microsoft SharePoint
- Elastic Search Connector

Prerequisites
-------------

- Python 3.13
- `.env` file with appropriate API keys and configuration variables

Installation
------------

To install the `elsai-cloud-connectors` package:

.. code-block:: bash

   pip install --index-url https://elsai-core-package.optisolbusiness.com/root/elsai-cloud-connectors/ elsai-cloud-connectors==0.1.0

Components
----------

1. AwsS3Connector
~~~~~~~~~~~~~~~~~

`AwsS3Connector` is a class for interacting with AWS S3 buckets, enabling secure upload, download, and deletion of files.

.. code-block:: python

   from elsai_cloud.aws import AwsS3Connector

   s3_client = AwsS3Connector(
       access_key="your_access_key",
       secret_key="your_secret_key",
       session_token="your_session_token"
   )  # Or use environment variables: AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_SESSION_TOKEN

    # Upload a local file to the specified S3 bucket and key (path in S3)

   s3_client.upload_file_to_s3(
       bucket_name="your_bucket_name",
       s3_key="your_s3_key",
       file_path="path/to/your/file.txt"
   )

    # Download a file from the specified S3 bucket and key to a local path

   s3_client.download_file_from_s3(
       bucket_name="your_bucket_name",
       file_name="your_s3_key",
       download_path="path/to/download/file.txt"
   )
 
    # Delete a file from the specified S3 bucket

   s3_client.delete_file_from_s3(
       bucket_name="your_bucket_name",
       s3_key="your_s3_key"
   )

**Required Environment Variables:**

- ``AWS_ACCESS_KEY_ID`` – Your AWS access key ID  
- ``AWS_SECRET_ACCESS_KEY`` – Your AWS secret access key  
- ``AWS_SESSION_TOKEN`` – Temporary session token for authentication  

2. AzureBlobStorage
~~~~~~~~~~~~~~~~~~~

`AzureBlobStorage` is a class for downloading files from Azure Blob containers.

.. code-block:: python

   from elsai_cloud.azureblobstorage import AzureBlobStorage

   azure_blob_client = AzureBlobStorage(connection_string="your_connection_string")

   azure_blob_client.download_file(
       container_name="your_container_name",
       blob_name="your_blob_name",
       target_folder_path="path/to/download/folder"
   )

3. MSGraphWebhooks
~~~~~~~~~~~~~~~~~~

`MSGraphWebhooks` helps manage webhook subscriptions for Microsoft Graph API resources.

.. code-block:: python

   from elsai_cloud.microsoft_webhooks import MSGraphWebhooks

   ms_graph = MSGraphWebhooks(
       client_id="your_client_id",
       tenant_id="your_tenant_id",
       client_secret="your_client_secret"
   )  # Or use environment variables: CLIENT_ID, TENANT_ID, CLIENT_SECRET

    
    # Create a new subscription (webhook) to listen for changes on a resource
   ms_graph.create_subscription(
       change_type="change_type",
       notification_url="https://webhook.example.com/send-notifications",
       resource="me/mailFolders('Inbox')/messages",
       expiration_date_time="2016-11-20T18:23:45.9356913Z",  # datetime format
       client_state="custom_state_123"
   )

    # Retrieve details of a specific subscription by its ID
   subscriptions = ms_graph.get_subscription(subscription_id="your_subscription_id")


    # List all current active subscriptions for the authenticated app
   subs_list = ms_graph.list_subscriptions()

    # Update an existing subscription's expiration or notification URL
   ms_graph.update_subscription(
       subscription_id="subscription_id",
       notification_url="https://webhook.example.com/send-notifications",
       expiration_date_time="2016-11-20T18:23:45.9356913Z"
   )


    # Delete a subscription by its ID to stop receiving notifications
   ms_graph.delete_subscription(subscription_id="subscription_id")


**Required Environment Variables:**

- ``TENANT_ID`` – Azure Active Directory tenant identifier used for authentication.  
- ``CLIENT_ID`` – Application (client) ID registered in Azure AD.  
- ``CLIENT_SECRET`` – Client secret generated for the Azure AD app to authorize access.  


4. OneDriveService
~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from elsai_cloud.onedrive import OneDriveService

   one_drive_service = OneDriveService(
       tenant_id="your_tenant_id",
       client_id="your_client_id",
       client_secret="your_client_secret"
   )  # Or set in environment variables

    # Get the unique Microsoft user ID associated with the email address
   user_id = one_drive_service.get_user_id(email="your_mail_address")


    # Upload a local file to a specified folder in the OneDrive of the given user
   one_drive_service.upload_file_to_onedrive(
       email="your_mail_address",
       local_file_path="path/to/your/file.txt",
       folder_path="path/to/folder/in/onedrive"
   )

    # Retrieve a list of files from a specific folder in the user's OneDrive
   files = one_drive_service.retrieve_onedrive_files_from_folder(
       email="your_mail_address",
       folder_path="path/to/folder/in/onedrive"
   )

    # Download a specific file from the user's OneDrive to a local directory
   one_drive_service.download_file_from_onedrive(
       email="your_mail_address",
       file_id="your_file_id",
       target_folder="path/to/download/folder"
   )

**Environment Variables:**

- ``TENANT_ID`` – Azure Active Directory tenant identifier used for authentication.  
- ``CLIENT_ID`` – Application (client) ID registered in Azure AD.  
- ``CLIENT_SECRET`` – Client secret generated for the Azure AD app to authorize access.  

5. SharePointService
~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from elsai_cloud.sharepoint import SharePointService

   sharepoint_service = SharePointService(
       tenant_id="your_tenant_id",
       client_id="your_client_id",
       client_secret="your_client_secret",
       site_hostname="your_site_hostname",
       site_path="your_site_path",
       drive_name="your_drive_name",
       drive_id="your_drive_id"
   )  # Or set in environment variables

    # Upload a local file to a specified folder in SharePoint
   sharepoint_service.upload_file_to_sharepoint(file_path="path/to/your/file.txt", target_folder="Documents/FolderName")

    # Retrieve a list of files from a specific folder in SharePoint
   files = sharepoint_service.retrieve_sharepoint_files_from_folder(folder_name="folderName")

    # Download a specific file from SharePoint to a local directory
   sharepoint_service.download_file_from_sharepoint(file_id="your_file_id", target_folder="path/to/download/folder")

**Environment Variables:**

- ``TENANT_ID`` – Azure Active Directory tenant identifier used for authentication.  
- ``CLIENT_ID`` – Application (client) ID registered in Azure AD.  
- ``CLIENT_SECRET`` – Client secret generated for the Azure AD app to authorize access.  
- ``SITE_HOSTNAME`` – SharePoint domain (e.g., ``yourcompany.sharepoint.com``).  
- ``SITE_PATH`` – Path to the SharePoint site (e.g., ``/sites/yoursite``).  
- ``DRIVE_NAME`` – Name of the document library (usually ``Documents``).  
- ``DRIVE_ID`` – Unique identifier for the SharePoint drive within the site.


6. ElasticSearch
~~~~~~~~~~~~~~~~

`ElasticSearchConnector` is used for interacting with an Elasticsearch index using API keys.

.. code-block:: python

   from elsai_cloud.elastic_search import ElasticSearchConnector

   es_connector = ElasticSearchConnector(
       cloud_url="your_cloud_url",
       api_key="your_api_key"
   )  # Or use environment variables: ELASTIC_SEARCH_URL, ELASTIC_SEARCH_API_KEY


   # Add a document
   doc = {
       "text": "This is a sample document to be indexed in Elasticsearch.",
   }

   es_connector.add_document(index_name="sampleindex", document=doc, doc_id="1")


   # Retrieve a document
   retrieved_doc = es_connector.get_document(index_name="sampleindex", doc_id="1")


   # Search documents
   search_doc = es_connector.search_documents(
       index_name="sampleindex",
       query={"match": {"text": "sample"}}
   )

**Environment Variables:**

- ``ELASTIC_SEARCH_URL`` – URL of the Elasticsearch cloud instance  
- ``ELASTIC_SEARCH_API_KEY`` – API key for authenticating with Elasticsearch


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

Elsai NLI
=========

The **Elsai NLI** (Natural Language Interface) package enables users to ask natural language questions directly over structured data sources like CSV files using LLM-powered agents.

Prerequisites
-------------

- Python 3.13

Installation
------------

To install the `elsai-nli` package:

.. code-block:: bash

   pip install --index-url https://elsai-core-package.optisolbusiness.com/root/elsai-nli/ elsai-nli==0.1.0

Component
---------

1. CSVAgentHandler
~~~~~~~~~~~~~~~~~~

`CSVAgentHandler` is a class that allows querying CSV files using natural language. It leverages an LLM and an agent interface to convert questions into structured operations.

.. code-block:: python

   from elsai_nli.natural_language_interface import CSVAgentHandler

   agent = CSVAgentHandler(
       csv_files="path_to_csv",  # Can be a single file path or a list of paths
       model="llm_model",
       verbose=True,
       agent_type="OPENAI_FUNCTIONS"
   )

   response = agent.ask_question("What is the total sales amount for each product?")

**Required Parameters:**

- ``csv_files`` – Path or list of paths to CSV files to be queried  
- ``model`` – Identifier or instance of the LLM to be used  
- ``agent_type`` – Type of agent backend (e.g., `OPENAI_FUNCTIONS`)  
- ``verbose`` – *(Optional)* Enables debug/log output during execution




Elsai Speech-to-Text
====================

The **Elsai Speech-to-Text** package provides an interface to transcribe audio using **Azure OpenAI Whisper**, enabling high-quality transcription of spoken content into text.

Prerequisites
-------------

- Python 3.13
- `.env` file with Azure OpenAI Whisper credentials:

Installation
------------

To install the `elsai-stt` package:

.. code-block:: bash

   pip install --index-url https://elsai-core-package.optisolbusiness.com/root/elsai-stt/ elsai-stt==0.1.0

Component
---------

1. AzureOpenAIWhisper
~~~~~~~~~~~~~~~~~~~~~

`AzureOpenAIWhisper` is a class used to transcribe audio using Azure’s hosted version of OpenAI Whisper. You can provide credentials directly or through environment variables.

.. code-block:: python

   from elsai_stt.azure_openai import AzureOpenAIWhisper

   whisper = AzureOpenAIWhisper(
       api_version="your_api_version",
       endpoint="azure_whisper_endpoint",
       api_key="api_key",
       deployment_id="deployment_id"
   )  # Or set via environment variables

   # Path to the audio file
   test_file = "harvard.wav"

   # Transcribe audio
   result = whisper.transcribe_audio(file_path=test_file)

**Required Environment Variables:**

- ``AZURE_OPENAI_API_VERSION`` – Version of the Azure OpenAI API  
- ``AZURE_OPENAI_ENDPOINT`` – Endpoint URL for Azure Whisper deployment  
- ``AZURE_OPENAI_API_KEY`` – API key for authenticating requests  
- ``AZURE_OPENAI_DEPLOYMENT_ID`` – Deployment ID for the Whisper model


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




