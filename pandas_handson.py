import pandas as pd
#Q1. create a dictionary with 5key values pair? and convert the data into pandas series?
dic={'name':'aryan','rollno':95,'class':'bca','city':'faridabad','state':'haryana'}
df=pd.Series(dic)
print(df)
#Q2. create a sample series with 10 no?
# a)print the first 5 elements
# b)print the last 5 elements 
# c)update 5th index with value 20
# d)delete the 1st element
df=pd.Series([1,2,3,4,5,6,7,8,9,10])
print(df)
print(df.head())
print(df.tail())
#or
print(df[:5])
print(df[5:])
df[5]=20
print(df[5])
df.drop(0)
#Q3. create a nested list, nested dict(store the values in the form of a list ), create atleast 3keys ?
nested_list=[['aryan',95,'bca'],['gurudas',106,'bca'],['amar',119,'bca']]
df=pd.DataFrame(nested_list,columns=['name','rollno','course'])
print(df)
#Q4. create a dataframe using the dictionary having atleast 3 values in each series of the dataframe
dict={
    'car':['thar','scorpio','wagonr'],
    'price':[10,20,30,],
    'model':[2011,2012,2013]
}
df=pd.DataFrame(dict)
print(df)
#a)rename the car to model
df=df.rename(columns={'car':'mode'})
print(df)
df=df.rename(columns={'model':'year'})
print(df)
#b) select all the rows where year is greater than 2011
print(df[df['year'] > 2011])
#Q5.a) Select all the rows where model is BMW and year is greater than 2010
print(df[(df['mode']=='thar') & (df['year']>2010)])
#b) select all the rows where model is thar or year is smaller than 2012
print(df[(df['mode']=='thar') | (df['year'] < 2012)])
#   Q5. create a dataframe with two columns ['name']['age']?
#   b)  in each column put atleast 7 values 
#   c)  print the first 8 rows 
#   d)  print the last 8 rows
#   e)  update the 5th row ->['john',80]
#   f)  print all the rows where age is 30?
data={'name':['aryan','gurudas','amar','ronit','sumit','sadil','krishna','ayush'],
      'age' :[18,19,21,19,20,22,17,19]}
df=pd.DataFrame(data)
print(df)
print(df[df.index<8])
print(df[:8])
print(df[2:])
df.loc[5]=['john',18]
print(df)
print(df[df['age']>19])

