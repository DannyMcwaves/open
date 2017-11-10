from open.main.pdf import Pdf
from open.main.variables import PDF_DATA

pdf = Pdf(PDF_DATA, 'rb')
pdf2 = Pdf(open(PDF_DATA, 'rb'))
print(pdf.file)
print(pdf2.file)
