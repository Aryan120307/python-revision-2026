
#  pandas is a pyhton library used for working with datasets ,it has functions for :
# 1. analyzing 
# 2. cleaning
# 3. exploring and manipulating data 
# pandas - tables
# numpy - matrices
# series-individual column are called series in pandas 
# data frames- collection  of series are known as dataframes or table
import pandas as pd
ser=pd.Series([10,20,30,40,50],name='ages')
print(ser)
# another way for creating series
d1={'a':100,'b':200,'c':300,'d':400}
ser2=pd.Series(d1,name='marks')
print(ser2)
#can change index of series 
ser=pd.Series([10,20,30,40,50],index=['a','b','c','d','e'],name='ages')
print(ser)
#creation of dataframes
lst=[[1,2,3],[4,5,6]]
df=pd.DataFrame(lst,columns=['class','roll','age'],index=['a','b'])
print(df)
#now making a student record
lst=[['Aryan',18,'BCA'],['Gurudas',18,'BCA'],['Amar',19,'BCA']]
df=pd.DataFrame(lst,columns=['Name','Age','Course'],index=['s1','s2','s3'])
print(df)
#most popular way of creating dataframe is by using dictionary
data={'Name':['Aryan','Gurudas','Amar'],'Age':[18,18,19],'Course':['BCA','BCA','BCA']}
df=pd.DataFrame(data,index=['s1','s2','s3'])
print(df)
#accessing specific columns from dataframe
print(df['Name'])
print(df['Age'])
# #accessing specific rows from dataframe
print(df.loc['s2'])
#join() - the join() is used to combine columns of two dataframe based on common column or index
data1={'alpha_left':['a','b','c','d'],'number':[1,2,6,5],'alphanumeric_left':['a','b','c','d']}
df1=pd.DataFrame(data1)
data2={'alpha_right':['a','b','c','d'],'number':[5,6,7,8],'alphanumeric_right':['e5','f6','g7','h8']}
df2=pd.DataFrame(data2)
print(df1)
print(df2)
#inner join
df_inner=pd.merge(df1,df2,on='number',how='inner')
print(df_inner)
#outer join
df_outer=pd.merge(df1,df2,on='number',how='outer')
print(df_outer)
#left join
df_left=pd.merge(df1,df2,on='number',how='left')
print(df_left)
#right join 
df_right=pd.merge(df1,df2,on='number',how='right')
print(df_right)