from PyPDF2 import PdfFileWriter, PdfFileReader

#PIP INSTALL PYPDF2

pages_to_keep = [2] # page numbering starts from 0

for j in range(1,157):
    infile = PdfFileReader('C:\\PDFS\\ARQUIVO (' + str(j) + ').pdf', 'rb')
    output = PdfFileWriter()
    for i in pages_to_keep:
        p = infile.getPage(i)
        output.addPage(p)
    with open('C:\\PDFS\\RESULTADO-' + str(j) + '.pdf', 'wb' ) as f:
        output.write(f)
