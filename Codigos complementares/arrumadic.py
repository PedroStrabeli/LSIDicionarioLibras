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

txtData1 = open("lista6.txt", 'r', encoding="utf8")
txtData2 = open("lista7.txt", 'w', encoding="utf8")

i=0
for line in txtData1:

    #line = line.replace('SimpleXMLElement Object ( [item] => SimpleXMLElement Object ( [@attributes] => Array ( [descricao] => ', '')
    #line = line.replace(' [exemploPortugues] => ', ',,')
    #line = line.replace(" [video] => ", ",,")
    #line = line.replace(' [classe] => ', ",,")
    #line = line.replace(' [mao] => ', ",,")
    #line = line.replace(' [origem] => ', ",,")
    #line = line.replace(' [libras] => ', ",,")
    #line = line.replace(' ) ) ) ', ",,")
    #line = line.replace(',,SimpleXMLElement Object ( [0] => ) ', "")


    #line = line.replace('<item descricao="', ',,')
    #line = line.replace('" exemploPortugues="', ',,')
    #line = line.replace('" video="', ',,')
    #line = line.replace('" classe="', ',,')
    #line = line.replace('" mao="', ',,')
    #line = line.replace('" origem="', ',,')
    #line = line.replace('" libras="', ',,')
    #line = line.replace('"/>', ',,')
    if (i%2==0):    
        txtData2.write(line)
    i=i+1

txtData1.close()
txtData2.close()
