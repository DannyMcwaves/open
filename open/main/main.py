from open.main.pdf import Pdf
from open.main.variables import PDF_DATA

pdf = Pdf(PDF_DATA, 'rb')
pdf2 = Pdf(open(PDF_DATA, 'rb'))

print(len(pdf))
print(bool(pdf2))
print(isinstance(Pdf, pdf))

print(pdf[-5])

for i in pdf:
    print(i)
