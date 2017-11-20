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
