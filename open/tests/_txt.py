from open import TXT_DATA
from open import Text

text = Text(TXT_DATA)

print(text)
print(len(text))
print(bool(text))
print(text.read())
print(text[1])
for i in text:
    print(i)

data = '''
this is more information that i want to append to the end of the file.
'''

state = text + data
print(state)
