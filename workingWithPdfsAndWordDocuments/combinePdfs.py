#! python3
# combinePdfs.py - Combines all the PDFs in the current working directory into a single PDF

import pypdf, os

# Get all the PDF filenames
pdfFiles = []

os.chdir(r'C:\Users\ogoay\OneDrive\Desktop\python_work\workingWithPdfsAndWordDocuments\New folder')

for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        pdfFiles.append(filename)
pdfFiles.sort(key = str.lower)

pdfWriter = pypdf.PdfWriter()


# Loop through all the PDF files
for filename in pdfFiles:
    pdfFile = open(filename, 'rb')
    pdfReader = pypdf.PdfReader(pdfFile)
    # Loop through all the pages (except the first and add them)
    for pageNum in range(1, pdfReader.get_num_pages()):
        pdfWriter.add_page(pdfReader.get_page(pageNum))

# Save the resulting PDF to a file
pdfOutput = open('allminutes.pdf', 'wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()