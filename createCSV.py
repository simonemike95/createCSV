import csv

inFile = input("File to read from: ")
outFile = input("Output to file: ")

f = open(inFile, "r")
fileText = f.read()
commaList = fileText.split(",") # Commas add a new column

outFile = outFile + ".csv"
f = open(outFile,'w')
f.write(fileText) # Line breaks start a new row

# with open(fileText, 'w', newline='\n') as myfile:
#      wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
#      wr.writerow(fileText)