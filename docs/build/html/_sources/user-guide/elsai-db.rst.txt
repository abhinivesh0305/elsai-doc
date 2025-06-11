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
