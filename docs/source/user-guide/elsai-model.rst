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
       max_tokens=500, #Default is 500
       temperature=0.1
   )  # Or set it as an environment variable

   llm = bedrockconnector.connect_bedrock(model_id="amazon.titan-text-express-v1")

**Required Environment Variables:**

- ``AWS_ACCESS_KEY_ID`` – Your AWS access key ID for authenticating with AWS services.
- ``AWS_SECRET_ACCESS_KEY`` – Your AWS secret access key for secure authentication.
- ``AWS_SESSION_TOKEN`` – Temporary session token for secure AWS authentication (used with IAM roles or temporary credentials).
- ``AWS_REGION`` – AWS region (e.g., us-east-1) where the Bedrock service is hosted.
- ``BEDROCK_TEMPERATURE`` – Controls the randomness of the output from the model (optional; default can be set in code).