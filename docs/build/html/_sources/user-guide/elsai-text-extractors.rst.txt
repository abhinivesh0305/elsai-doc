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