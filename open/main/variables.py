
__all__ = ['PDF_DATA', 'CSV_DATA', 'TXT_DATA', 'JSON_DATA', 'JSON_DATA2', 'XML_DATA']

import os
directory = os.path.dirname(__file__)


# sample read write data
PDF_DATA = os.path.abspath(os.path.join(directory, '../data/pdf-sample.pdf'))
CSV_DATA = os.path.abspath(os.path.join(directory, '../data/csv-sample.csv'))
TXT_DATA = os.path.abspath(os.path.join(directory, '../data/text-sample.txt'))
JSON_DATA = os.path.abspath(os.path.join(directory, '../data/companies.json'))
JSON_DATA2 = os.path.abspath(os.path.join(directory, '../data/zips.json'))
XML_DATA = os.path.abspath(os.path.join(directory, '../data/volume.xml'))


# open modes.
READ_ONLY = 'r'
READ_BINARY = 'rb'
WRITE_ONLY = 'w'
WRITE_BINARY = 'wb'
READ_WRITE = 'r+'
READ_WRITE_BINARY = 'a+b'
