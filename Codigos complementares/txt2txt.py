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
txtData2 = open("videos.txt", 'w', encoding="utf8")

a1="%C1"
a2='%C0'
a3='%C3'
a4='%C2'
a5='%CA'
a6='%C9'
a7='%C8'
a8='%CC'
a9='%CD'
aa='%CE'
ab='%D2'
ac='%D3'
ad='%D4'
af='%D5'
ah='%D9'
ai='%DA'
aj='%DB'
ak='%C7'
i=0
for line in txtData1:
    #line = line.replace('.JPG', '')
    #line = line.replace('"/>', ',')
    #line = line.replace("Á", a1)
    #line = line.replace('À', a2)
    #line = line.replace('Ã', a3)
    #line = line.replace('Â', a4)
    #line = line.replace('Ê', a5)
    #line = line.replace('É', a6)
    #line = line.replace('È', a7)
    #line = line.replace('Ì', a8)
    #line = line.replace('Í', a9)
    #line = line.replace('Î', aa)
    #line = line.replace('Ò', ab)
    #line = line.replace('Ó', ac)
    #line = line.replace('Ô', ad)
    #line = line.replace('Õ', af)
    #line = line.replace('Ù', ah)
    #line = line.replace('Ú', ai)
    #line = line.replace('Û', aj)
    #line = line.replace('Ç', ak)
    #line=line[0:-3]
    #print (line)
    #repartida = line.partition(',,')
    if(i%2==0):
        repartida = line.split(",,")
        #print (line)
        #print (repartida)
        video="http://www.acessobrasil.org.br/libras/filme/"+repartida[3]+"\n"
        txtData2.write(video)
        
    i=i+1

txtData1.close()
txtData2.close()
