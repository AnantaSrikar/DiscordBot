import requests
import PyPDF2
url = 'https://www.who.int/docs/default-source/coronaviruse/situation-reports/20200309-sitrep-49-covid-19.pdf'

def getInfo():

    try:
        myfile = requests.get(url)
        open('testfile.pdf', 'wb').write(myfile.content)
        pdfFileObj = open('testfile.pdf', 'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
        pageObj = pdfReader.getPage(4)
        data = pageObj.extractText()
        simplifiedData = data.split('\n')

        emptySpace = ' '
        for emptySpace in simplifiedData:
            try:
                simplifiedData.remove(emptySpace)
            except ValueError:
                pass
        indiaIndex = simplifiedData.index('India')
        textdata = 'Total Confirmed Cases = {}\nTotal Confirmed new cases = {}\nTotal Deaths = {}\nTotal new Deaths = {}\nTransmission Classification : {}\nDays since last report case : {}'.format(simplifiedData[indiaIndex + 1], simplifiedData[indiaIndex + 2], simplifiedData[indiaIndex + 3], simplifiedData[indiaIndex + 4], simplifiedData[indiaIndex + 5], simplifiedData[indiaIndex + 6])
        #dataFile = open('data.txt', 'r')
        pdfFileObj.close()
        return textdata
        #print(pdfReader.numPages)

    except PyPDF2.utils.PdfReadError:
        return ('Todays not yet released')

  
# printing number of pages in pdf file 
  
# creating a page object 
# pageObj = pdfReader.getPage(2) 
  
# extracting text from page 
# print(pageObj.extractText()) 
  
# closing the pdf file object 