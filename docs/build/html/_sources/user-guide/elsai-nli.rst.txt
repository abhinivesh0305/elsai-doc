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
