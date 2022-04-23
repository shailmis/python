import pandas as pd
#Creating a empty DataFrame
df = pd.DataFrame()
print (df)
#Creating a Dataframe from list
data = [1,4,6,67,54]
df = pd.DataFrame(data)
print (df)
#Creating a Dataframe from list - example2
data = [['Alex',10],['Bob',20],['Clarke',30]]
df = pd.DataFrame(data,columns=['Name','Age'])
print (df)

#Reading CSV file into panda's DataFrame
df=pd.read_csv('aapl.csv')
#print ( df)
#slicing of rows
print (df[2:20])
print (df.dtypes)
