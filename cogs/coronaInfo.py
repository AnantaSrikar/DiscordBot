import requests
import PyPDF2
url = 'https://www.who.int/docs/default-source/coronaviruse/situation-reports/20200304-sitrep-44-covid-19.pdf'
usl = 'https://www.who.int/docs/default-source/coronaviruse/situation-reports/20200303-sitrep-43-covid-19.pdf'

try:
    myfile = requests.get(url)
    open('testfile.pdf', 'wb').write(myfile.content)
    pdfFileObj = open('testfile.pdf', 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
    pdfFileObj.close() 

    print(pdfReader.numPages) 

except PyPDF2.utils.PdfReadError:
    print('Todays not yet released')

  
# printing number of pages in pdf file 
  
# creating a page object 
# pageObj = pdfReader.getPage(2) 
  
# extracting text from page 
# print(pageObj.extractText()) 
  
# closing the pdf file object 