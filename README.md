# OPEN
This python package currently supports opening Pdf, Csv, Json and Text files.


Import the opener function reader from the open package


`from open import opener, PDF_DATA, JSON_DATA`


**PDF_DATA :** sample pdf file


**JSON_DATA :** sample pdf file


`file = opener(PDF_DATA)`


*the opener uses mimetype detection to check the type of file and returns
 a specific reader object based on the type of the file*


## METHODS OF THE READER OBJECT

the reader provides an abstract base class to make sure all readers for different
file formats have the same methods.


```python
class OpenInterface:

    __slots__ = []
    __doc__ = ""
    __dict__ = {}

    @abstractmethod
    def __init__(file):
        '''gets the name of the file and initializes the object'''

    @abstractmethod
    def __iter__():
        '''iteration support'''

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


```

**NB:**
### file types supported or to be supoprted.
Read is going to be for CSV, PDF, JSON, pickleObject, dbm, text, shelve etc.
and sqlite3 maybe.
