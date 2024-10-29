#Extract text from pdf file python project

# need to install pypdf2 so run command pip install PyPDF2

import PyPDF2
pdf = open("dummy.pdf", "rb")
reader = PyPDF2.PdfReader(pdf)
page = reader.pages[0]
print(page.extract_text())
