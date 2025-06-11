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