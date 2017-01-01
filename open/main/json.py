"""
read, write and create json files
"""

__all__ = ['Json']

import json
from .interface import OpenInterface


class Json(OpenInterface):

    def __init__(self, file):
        super(Json, self).__init__(file)

    def read(self):
        """the reader for pdf"""

    def __len__(self):
        return self.file

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
        return self.file

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
            yield self.file

    def __radd__(self, other):
        """
        :param other:
        :return:
        """

    def write(self):
        """
        :return:
        """


