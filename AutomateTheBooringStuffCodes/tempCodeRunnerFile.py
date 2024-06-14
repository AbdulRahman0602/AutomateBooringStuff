import PyPDF2,os

pdf1file = open("Sample1.pdf","rb")
pdf2file = open("sample2.pdf","rb")

reader1 = PyPDF2.PdfReader("Sample1.pdf")
reader2 = PyPDF2.PdfReader("sample2.pdf")

writer = PyPDF2.PdfWriter()

for PageNum in range(len(reader1.pages)):
    page = reader1.pages[PageNum]
    writer.add_page(page)  

for PageNum in range(len(reader2.pages)):
    page = reader2.pages[PageNum]
    writer.add_page(page)  

outputFile = open("combined.pdf","wb")
writer.write(outputFile)
outputFile.close()
pdf1file.close()
pdf2file.close()