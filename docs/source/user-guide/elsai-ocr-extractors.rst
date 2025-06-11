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