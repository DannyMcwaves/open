"""
read, write and create csv documents.
"""

__all__ = ['Csv']

import csv
from .interface import OpenInterface


class Csv(OpenInterface):

    CONTAINER = []

    def __init__(self, file):
        super(Csv, self).__init__(file)
        self.csv_file_reader = csv.reader(self.file, delimiter=' ', quotechar='|')
        for i in self:
            self.CONTAINER.append(i)

    def __repr__(self):
        """
        :return:
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
        return self.CONTAINER

    def __len__(self):
        return len(self.CONTAINER)

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
        :return: None
        """
        for i in self.CONTAINER:
            print(i)

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
        return self.CONTAINER[item]

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
        yield from self.csv_file_reader

    def __radd__(self, other):
        """
        :param other:
        :return:
        """

    def write(self):
        """
        :return:
        """


