import discord 
from discord.ext import commands
import requests
import PyPDF2
#TODO : url = 'https://www.who.int/docs/default-source/coronaviruse/situation-reports/202003{}-sitrep-{}-covid-19.pdf'.format(d, n)
url = 'https://www.who.int/docs/default-source/coronaviruse/situation-reports/20200309-sitrep-49-covid-19.pdf'

class covCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command('covid')
    async def tester(self, ctx):
        #await ctx.channel.send('Stay tuned {}! COVID-19 update feature coming up soon.'.format(ctx.message.author.mention))
        await ctx.channel.send(getInfo())

def setup(bot):
    bot.add_cog(covCog(bot))

def getInfo():

    try:
        myfile = requests.get(url)
        open('res/testfile.pdf', 'wb').write(myfile.content)
        pdfFileObj = open('res/testfile.pdf', 'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
        pageObj = pdfReader.getPage(4)
        data = pageObj.extractText()
        simplifiedData = data.split('\n')

        emptySpace = ' '
        for emptySpace in simplifiedData:
            try:
                simplifiedData.remove(' ')
            except ValueError:
                pass
        indiaIndex = simplifiedData.index('India')
        textdata = 'Data for India :\n' + 'Total Confirmed Cases = {}\nTotal Confirmed new cases = {}\nTotal Deaths = {}\nTotal new Deaths = {}\nTransmission Classification : {}\nDays since last report case : {}'.format(simplifiedData[indiaIndex + 1], simplifiedData[indiaIndex + 2], simplifiedData[indiaIndex + 3], simplifiedData[indiaIndex + 4], simplifiedData[indiaIndex + 5], simplifiedData[indiaIndex + 6])
        #dataFile = open('data.txt', 'r')
        pdfFileObj.close()
    
        return textdata
        #print(pdfReader.numPages)

    except PyPDF2.utils.PdfReadError:
        return ('Todays not yet released')