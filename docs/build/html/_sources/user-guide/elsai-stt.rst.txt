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