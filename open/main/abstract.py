import abc


class OpenFace(abc.ABC):

    @abc.abstractmethod
    def read(self):
        """this official read format for files"""
