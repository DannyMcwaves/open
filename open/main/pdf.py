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

    def __repr__(self):
        """
        :return: class name and file name.
        """
        return '<{0} file="{1}" mode="{2}">'.format(self.__class__.__name__, self.file.name, self.file.mode)

    def __copy__(self):
        """
        :return:
        """

    def __deepcopy__(self, memodict={}):
        """
        :param memodict:
        :return:
        """

    def read(self):
        """the reader for pdf"""
        data = ""
        for i in self:
            data += i
        return data

    def __len__(self):
        return self.pdf_file_read.getNumPages()

    def __add__(self, other):
        """
        :param other:
        :return:
        """

    def __bool__(self):
        """
        :return: true || false
        """
        return bool(len(self))

    def __call__(self, *args, **kwargs):
        """
        :param args:
        :param kwargs:
        :return:
        """
        return self.read()

    def __contains__(self, item):
        """
        :param item:
        :return:
        """

    def __enter__(self):
        """
        :return:
        """

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        :param exc_type:
        :param exc_val:
        :param exc_tb:
        :return:
        """

    def __getitem__(self, item):
        """
        :param item:
        :return:
        """
        if type(item) != int or item > len(self) or item < 0:
            return NotImplemented
        return self.pdf_file_read.getPage(item).extractText()

    def __iadd__(self, other):
        """
        :param other:
        :return:
        """

    def __instancecheck__(self, instance):
        """
        :param instance:
        :return:
        """
        return isinstance(self, instance)

    def __iter__(self):
        """
        :return:
        """
        for i in range(len(self)):
            yield self.pdf_file_read.getPage(i).extractText()

    def __radd__(self, other):
        """
        :param other:
        :return:
        """

    def write(self):
        """
        :return:
        """
