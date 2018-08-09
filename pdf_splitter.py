import os
from PyPDF2 import PdfFileWriter, PdfFileReader
import glob
for filename in glob.glob('*.pdf'):
    name, ext = os.path.splitext(filename)
    inputpdf = PdfFileReader(open(filename, "rb"))

    for i in range(inputpdf.numPages):
        output = PdfFileWriter()
        output.addPage(inputpdf.getPage(i))
        with open('{}_page{}{}'.format(name, i+1, ext), "wb") as outputStream:
            output.write(outputStream)
