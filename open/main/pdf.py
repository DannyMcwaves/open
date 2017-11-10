"""
this should a class that contains as many utility functions as possible for reading,
writing data from pdf files.
"""

__all__ = ['Pdf']


import PyPDF2
from .interface import OpenInterface
from .variables import READ_WRITE_BINARY


class Pdf(OpenInterface):

    def __init__(self, file, action=READ_WRITE_BINARY):
        super(Pdf, self).__init__(file, action)
        self.pdf_file_read = PyPDF2.PdfFileReader(self.file)

    def read(self):
        """the reader for pdf"""
