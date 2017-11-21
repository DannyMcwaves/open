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
class Reader:
    def __init__(file):
        '''gets the name of the file and initializes the object'''

    def __iter__():
        '''iteration support'''
```

**NB:**
### file types supported or to be supoprted.
Read is going to be for CSV, PDF, JSON, pickleObject, dbm, text, shelve etc.
and sqlite3 maybe.
