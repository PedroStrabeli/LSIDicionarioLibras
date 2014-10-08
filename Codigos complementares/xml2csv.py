# xml2csv.py
# Convert all CSV files in a given (using command line argument) folder to XML.
# FB - 20120523
# First row of the csv files must be the header!
# example CSV file: myData.csv
# id,code name,value
# 36,abc,7.6
# 40,def,3.6
# 9,ghi,6.3
# 76,def,99
import sys
import os
import csv
import xml
if len(sys.argv) != 2:
    os._exit(1)
path=sys.argv[1] # get folder as a command line argument
os.chdir(path)
xmlFiles = [f for f in os.listdir('.') if f.endswith('.xml') or f.endswith('.XML')]
for xmlFile in xmlFiles:
    csvFile = xmlFile[:-4] + '.csv'
    csvData = xml.reader(open(xmlFile))
    csvData = open(csvFile, 'w')
    
    rowNum = 0
    for row in xmlData:
        if rowNum == 0:
            tags = row
            # replace spaces w/ underscores in tag names
            for i in range(len(tags)):
                tags[i] = tags[i].replace(' ', '_')
        else: 
            xmlData.write('<row>' + "\n")
            for i in range(len(tags)):
                xmlData.write('    ' + '<' + tags[i] + '>' \
                              + row[i] + '</' + tags[i] + '>' + "\n")
            xmlData.write('</row>' + "\n")                
        rowNum +=1

    xmlData.close()
