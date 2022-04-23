import csv

filename = "aapl.csv"
fields = []
rows = []
print("File Name" + filename)

with open(filename,'r') as FILE:
    #create a CSVReader object from file Object FILE
    csvreader=csv.reader(FILE)
    fields = next(csvreader)
    print (fields)
    for row in csvreader:
        rows.append(row)
    print("total number of rows : %d" %(csvreader.line_num))

    print("fields names are:" + ','.join(field for field in fields))
    print ("Test".join(field for field in fields))
    print("\n First 5 rows are:\n")
    for row in rows[:5]:
        #parsing each column of a row
        for col in row:
            # To supress new line add , end = ' ' in the print statement
            print("%10s"%col,end = '')
        print ('\n')
            

