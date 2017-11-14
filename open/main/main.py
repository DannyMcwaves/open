from open.main.pdf import Pdf
from open.main.txt import Text
from open.main.variables import PDF_DATA, TXT_DATA

pdf = Pdf(PDF_DATA)
pdf2 = Pdf(open(PDF_DATA, 'rb'))
text = Text(TXT_DATA)


print(len(pdf))
print(bool(pdf2))
print(isinstance(Pdf, pdf))
print(text.read())

print(pdf[-5])

for i in pdf:
    print(i)
