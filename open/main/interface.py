"""
UML for abstract interface for all read-writer objects.

    properties.
        * __slots__

    methods
        * __len__ returns the of the file [number of pages or number of lines]
        * __iter__ for loops
        * __getitem__ get a particular page or a particular line.
        * __setitem__ change the content for a particular line or page.
        * __enter__ context support.
        * __exit__ context support.
        * __add__ write support to add data to the file object.
        * __radd__ this file plus another file || content.
        * __repr__ object representation.
        * __instancecheck__ check for instances of this object.
        * __call__
        * __contains__
        * __iadd__
        * __copy__
        * __deepcopy__
        * __bool__

        * read returns the entire file content.
        * write write into the file object.
"""

__all__ = ['OpenInterface']

from abc import abstractmethod, ABC
from io import TextIOBase, BufferedIOBase
from .variables import READ_WRITE


class OpenInterface(ABC):

    __slots__ = []
    __doc__ = ""
    __dict__ = {}

    @abstractmethod
    def __init__(self, file, action=READ_WRITE):
        """all object should be initialized with a name """
        self.file = file if isinstance(file, TextIOBase) or isinstance(file, BufferedIOBase) else open(file, action)

    @abstractmethod
    def read(self):
        """this official read format for files"""

    @abstractmethod
    def write(self):
        """write formats for data"""

    @abstractmethod
    def __iter__(self):
        """
        all objects should support iteration
        :return yield. support iteration.
        """

    @abstractmethod
    def __len__(self):
        """
        the number of lines or the number of pages a document has
        :return number of pages or lines.
        """

    @abstractmethod
    def __enter__(self):
        """
        self context manager that returns the object itself.
        :return: self.
        """

    @abstractmethod
    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        exit the context manager.
        :param exc_type:
        :param exc_val:
        :param exc_tb:
        :return: True
        """

    @abstractmethod
    def __getitem__(self, item):
        """
        get specific page or line.
        :param item: page or line number.
        :return: page or line content
        """

    @abstractmethod
    def __add__(self, other):
        """
        add with another file or content.
        :param other:
        :return: None
        """

    @abstractmethod
    def __radd__(self, other):
        """
        add to this file to another file.
        :param other: another file.
        :return: None
        """

    @abstractmethod
    def __call__(self, *args, **kwargs):
        """
        when an instance is called.
        :param args:
        :param kwargs:
        :return: None
        """

    @abstractmethod
    def __iadd__(self, other):
        """
        add another file or content to this.
        :param other: file or content.
        :return: None.
        """

    @abstractmethod
    def __contains__(self, item):
        """
        uses regex pattern matching to find item
        :param item:
        :return: boolean.
        """

    @abstractmethod
    def __bool__(self):
        """
        if object is empty or not
        :return: boolean
        """

    def __repr__(self):
        """
        string representation of the object class.
        :return: string repr.
        """

    @abstractmethod
    def __instancecheck__(self, instance):
        """
        check for instances
        :param instance: instance object.
        :return: boolean
        """

    def __copy__(self):
        """
        shallow copy the content of the file object.
        :return: shallow copy object
        """

    def __deepcopy__(self, memodict={}):
        """
        return deep copy of the file object content.
        :param memodict: memory dict.
        :return: deep copied object.
        """