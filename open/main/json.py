"""
read, write and create json files
"""

__all__ = ['Json']

import json
from .interface import OpenInterface


class Json(OpenInterface):

    def __init__(self, file):
        super(Json, self).__init__(file)

