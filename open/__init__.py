"""
this is the main initializer for the whole package.
provides top level access for the important variables available in the entire package
including classes, functions and data variables.
"""

__all__ = ['opener', 'Json', 'Pdf', 'Csv', 'Text', 'JSON_DATA', 'PDF_DATA', 'XML_DATA', 'CSV_DATA', 'TXT_DATA', 'JSON_DATA2']


from .main import opener, Json, Pdf, Text, Csv, JSON_DATA, PDF_DATA, TXT_DATA, CSV_DATA, XML_DATA, JSON_DATA2
