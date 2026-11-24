#! python3
# decryptPdfs2.py - uses a given password to attempt decrypting all encrypted PDFs in a folder and all its subfolders 

import os, pypdf

os.chdir(r'C:\Users\ogoay\OneDrive\Desktop\python_work\workingWithPdfsAndWordDocuments\New folder')             # change directory to the folder with the encrypted files we wish to decrypt

for folder, subfolder, filenames in os.walk(os.curdir):     # loop through all subfolders and files in the current directory                    
    for filename in filenames:                              # loop through all the files
        if filename.endswith('.pdf'):              # select only encrypted pdf files
            directory = os.path.abspath(folder + os.path.sep + filename)        # store the absolute path of the filename in the variable directory
            pdfFile = open(directory, 'rb')                 # open a pdf file object of the current file
            reader = pypdf.PdfReader(pdfFile)               # create a reader object of the file
            try: 
                reader.get_page(0)                          # check if pdf file is encrypted
            except pypdf.errors.FileNotDecryptedError:      # if pdf file is encrypted
                try:
                    reader.decrypt('password')                      # pass the decryption password to the reader object 
                    writer = pypdf.PdfWriter()                      # create a pdf writer object
                    for pageNum in range(reader.get_num_pages()):   # loop through all the pages in the pdf file
                        writer.add_page(reader.get_page(pageNum))   # add each page to the pdf writer object
                    resultPdf = open(f'{folder}{os.path.sep}{filename.split('.pdf')[0]}_decrypted.pdf', 'wb')             # create an output pdf file to store the contents of pdf writer
                    writer.write(resultPdf)             # write the contents of the pdf writer to the new pdf file
                    resultPdf.close()
                    pdfFile.close()
                except pypdf.errors.FileNotDecryptedError:          # if decryption password does not work
                    print(f'Incorrect password for {filename} in {directory.split(filename)[0]}')           # print incorrect password back to the user

print('Done')

