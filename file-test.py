file = open("access1.log","r")
lines = file.readlines()
l = list()

for line in lines:
    line = line.strip()
    print (len(line))
    #l = line.split(' ')[2]
    #print (l)
