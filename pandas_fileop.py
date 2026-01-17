import pandas as pd
import numpy as np
#read a csv file
dfo=pd.read_csv('mtcars.csv')
#print full list 
print(dfo)
#print first 5 rows
print(dfo.head())
#print last 5 rows
print(dfo.last)
#print shape of dataframe
print(dfo.shape)
#print information about dataframe
print(dfo.info())
#print null values in each column 
print(dfo.isnull().sum())
#print statistical summary of df
print(dfo.describe())
#print mean of column cyl
print(dfo.cyl.mean())
# #rename column name from mpg to miles per gallon
df=dfo.rename(columns={'mpg':'miles per gallon'},inplace='True')
df=dfo.rename(columns={'cyl':'cy'},inplace='True')
print(dfo)
print(dfo.head())
# # slicing the dataframe 
print(dfo[4:20][['cy','hp']])
print(dfo[0:4][['cy','hp']])
# #Another way of slicing 
# #iloc(integer location) - where we use index format to mention column no asa well
print(dfo.iloc[4:20,2:5])
print(dfo.iloc[0:4,0:2])
#loc - slice through labels only in row and column
print(dfo.loc[4:20,'miles per gallon':'cy'])
#adding a new column 
lst=np.arange(1,33,1)
dfo['newcolumn']=lst
print(dfo.head())
#sort dataframe by column cy in descending 
print(dfo.sort_values(by='cy',ascending=True))
print(dfo.sort_values(by='miles per gallon',ascending=True))
#filtering on string condition
print(dfo[dfo['model'].isin(['Mazda RX4','Ferrari Dino'])])
print(dfo[dfo['model'].isin(['Fiat 128','Honda Civic'])])
#another way
print(dfo[dfo['model'].str.contains('Mazda|Honda')])
print(dfo[dfo['model'].str.contains('Toyota')])
#create a column with length of strings in model column
df['length_model_names']=df.model.apply(len)