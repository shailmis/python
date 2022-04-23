#!/usr/bin/env python
# coding: utf-8

# In[29]:


file = open ('fruits.txt',"r")
#Declare dictionary object
d = dict()

lines = file.readlines()
for line in lines:
    #remove trailing new line
    line = line.strip()
    #convert lower case
    line = line.lower()
    words = line.split(" ")
    for word in words:
        #if word is present in Dictionary then add counter 
        #by one else add word in the dictionary with value 1
        if word in d:
            d[word] = d[word] + 1
        else:
            d[word] = 1
print (d)
    
file.close()


# In[ ]:




