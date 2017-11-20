"""
this is the main interface to the main package that contains several utility functions for codes to be used by
different parts for the package and has the main export interface for the main package
"""

__all__ = ['opener', 'Json', 'Pdf', 'Csv', 'Text', 'JSON_DATA', 'PDF_DATA', 'XML_DATA', 'CSV_DATA', 'TXT_DATA', 'JSON_DATA2']

import mimetypes
import logging
from .json import Json
from .pdf import Pdf
from .csv import Csv
from .txt import Text
from .variables import JSON_DATA, PDF_DATA, CSV_DATA, TXT_DATA, XML_DATA, JSON_DATA2


logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

mimes = {
    'application/json': Json,
    'application/pdf': Pdf,
    'text/csv': Csv,
    'text/plain': Text
}

# disable all logs
logging.disable(logging.CRITICAL)


def opener(file):
    mime = mimetypes.guess_type(file)[0]
    reader = mimes.get(mime, None)
    logging.error(mime)
    return reader(file) if reader is not None else NotImplemented
