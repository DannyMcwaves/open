"""
this is going to contain tests from the file type detection
of the magic thingy.
"""
from open import JSON_DATA, PDF_DATA, CSV_DATA, TXT_DATA, XML_DATA
from open import opener

json = opener(JSON_DATA)
pdf = opener(PDF_DATA)
csv = opener(CSV_DATA)
txt = opener(TXT_DATA)
xml = opener(XML_DATA)

print(type(json))
