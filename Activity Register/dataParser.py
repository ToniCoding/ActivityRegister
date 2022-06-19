# This code is in charge of parsing data to pass it correctly to an XML file. It's also in charge of the following stuff:
    # >>> Adding an ID.
    # >>> Adding date to the entry that's passing.
    # >>> Adding time to the entry that's passing.

# Imports.
from datetime import datetime
from re import sub
from random import choice

# Date and time formatting to be XML schema compatible. Also, from here program takes the date to create the file.
now = datetime.now()
dateNow = now.strftime("%d/%m/%Y %H:%M:%S")
dateXML = now.strftime("%Y-%m-%d %H:%M:%S")
firstFormatting = sub(' ', 'T', dateXML)
fileNameFormatting = sub(':', '-', firstFormatting)
XMLFormatting = sub('/', '-', firstFormatting)

# File treatment of the current entry to be read.
xmlFileName = f'./registries/xml/regStorage/registry_{fileNameFormatting}.xml'
data = open('./registries/tempStorager/currentEntry.txt', 'r+')
xml = open(xmlFileName, 'a+')

# Treatment of the current entry data.
def dataParser():
    for x in data:
        attribs = x.split()
        regName = attribs[0]
        regCategory = attribs[1]
        wordCounter = 2
        entryProcessing = True
        itemList = []
        while entryProcessing == True: # Loop to treat and process entry.
            try:
                itemList.append(attribs[wordCounter])
                wordCounter+=1
            except IndexError:
                entryProcessing = False
        regEntry = ' '.join(itemList)
        regDate = XMLFormatting
        idRange = range(0,1000)
        regID = idRange[choice(idRange)]
    
    # Treatment for XML.
    def insertXMLReg(xml, regName, regCategory, regEntry, regDate, regID):
        insert = f'''<?xml version="1.0" encoding="UTF-8"?>
    <?xml-model href="../registrySchema.xsd" type="application/xml" schematypens="http://www.w3.org/2001/XMLSchema"?>
    <registries>
        <registry>
            <name>{regName}</name>
            <category>{regCategory}</category>
            <entry>{regEntry}</entry>
            <id>{regID}</id>
            <date>{regDate}</date>
        </registry>
    </registries>
        '''
    
        xml.write(insert)
    
    insertXMLReg(xml, regName, regCategory, regEntry, regDate, regID)