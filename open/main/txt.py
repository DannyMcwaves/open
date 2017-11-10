"""
read, write and create text file
"""

__all__ = ['Text']

from .interface import OpenInterface


class Text(OpenInterface):

    def __init__(self, file):
        super(Text, self).__init__(file)

