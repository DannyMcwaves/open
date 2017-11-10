"""
read, write and create csv documents.
"""

__all__ = ['Csv']

import csv
from .interface import OpenInterface


class Csv(OpenInterface):

    def __init__(self, file):
        super(Csv, self).__init__(file)

