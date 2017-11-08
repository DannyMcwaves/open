import abc


class OpenInterface(abc.ABC):

    def __init__(self):
        """all object should be initialized with a name """

    @abc.abstractmethod
    def read(self):
        """this official read format for files"""

    def write(self):
        """write formats for data"""

    def __iter__(self):
        """all objects should support iteration"""

    def __len__(self):
        """the number of lines or the number of pages a document has"""

