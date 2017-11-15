from open.main.variables import TXT_DATA
from open.main.txt import Text

text = Text(TXT_DATA)

print(text)
print(len(text))
print(text.read())
print(text[1])
for i in text:
    print(i)
