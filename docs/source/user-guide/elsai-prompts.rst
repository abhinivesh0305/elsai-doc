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
