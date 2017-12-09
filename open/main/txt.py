"""
read, write and create text file
"""

__all__ = ['Text']

from .interface import OpenInterface
from .variables import READ_WRITE


class Text(OpenInterface):

    def __init__(self, file, action=READ_WRITE):
        super(Text, self).__init__(file, action)
        self.text_file_read = self.file.readlines()

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
        return "".join(self.text_file_read)

    def __len__(self):
        return len(self.text_file_read)

    def __add__(self, other):
        """
        :param other:
        :return:
        """
        with self.file as file:
            file.write(other)
        return True

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
        return self.text_file_read[item]

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
        yield from self.text_file_read

    def __radd__(self, other):
        """
        :param other:
        :return:
        """

    def write(self, text):
        """
        :return:
        """
        self.file.write(text)
