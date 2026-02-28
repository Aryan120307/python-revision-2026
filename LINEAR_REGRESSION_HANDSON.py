#!/usr/bin/env python
# coding: utf-8

# # Linear Regression Handson

# In[29]:


#Agenda - Linear regression
#Supervised learning - it works upon proper label data on which our machine work on and predict the data 
#regression - predicting numerical values
# input / output
# here we finds a straight line relationship between the independent and dependent variable.


# In[30]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[31]:


df=pd.read_csv('insurance.csv')
df


# In[32]:


# EDA - exploratory data analysis
#null values
#duplicates
#outlier - to make my model biased free we need to remove the outliers
#label encoding


# In[33]:


df.info()


# In[34]:


df.isnull().sum().sum()


# In[35]:


df.duplicated().sum()


# In[36]:


#what if we had duplicates value :
#df.drop_duplicates(inplace=True)


# In[37]:


df.columns


# In[38]:


# for null values we have two option to fill na or to remove na.
#mode - categorical/object data as mode is more preferred option.
#mean - fill na with mean for data other than object data type


# In[39]:


for col in df.columns:
    if df[col].dtype=="object":
        df[col]=df[col].fillna(df[col].mode([0]))
    else:
        df[col]=df[col].fillna(df[col].mean())    


# In[40]:


# outlier(extreme values ) visualization


# In[41]:


for col in df.columns:
    if df[col].dtype !="object":
        sns.boxplot(df[col])
        plt.xlabel(col)
        plt.show()


# In[42]:


#outlier removal
outlist=['bmi','past_consultations','Hospital_expenditure','NUmber_of_past_hospitalizations','Anual_Salary']
for col in outlist:
    Q1=df[col].quantile(0.25)
    Q3=df[col].quantile(0.75)
    IQR = Q3-Q1 #(interquartile range)
    LB= Q1 - 1.5*(IQR)
    UB= Q3 + 1.5*(IQR)
    df=df[(df[col] >=LB) & (df[col]<=UB)]



# In[43]:


df.info()


# In[45]:


# label encoding - convert categorical data or object into numeric data to make machine understand


# In[91]:


from sklearn.preprocessing import LabelEncoder


# In[92]:


LE=LabelEncoder()


# In[93]:


for col in df.columns:
    if (df[col].dtype == 'object'):
        df[col] = LE.fit_transform(df[col])


# In[94]:


# fit - learning the things
# transform - applying that learning


# In[95]:


df


# ***Now the EDA part is completed*** 

# ***MODEL BUILDING***
# 
# 1. Splitting the data into x(independent) and y(dependent/target).
# 
# 2. Splitting the data into the training and testing.
# 
# 3. Model initialization.
# 
# 4. Train the model.
# 
# 5. Prediction.
# 
# 6. Evaluation.

# In[96]:


# charges is my target column so i can except it or remove it 
x=df.iloc[:,:-1]
x
#x=df.drop(columns=['charges'])


# In[97]:


y=df['charges']
y


# In[98]:


from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,train_size=0.80,random_state=0)


# In[99]:


# 100 questions/solution
# i will give 80 question(x_train) with their solution(y_train)
# i have 20 questions with correct solution
# i am going to take a test
# i will give the student the test of 20 questions(x_test)
# the student will give some answer (correct /incorrect)(y_pred)
# i will compare the student answer with the correct answer that i have with me .
# compare y_test with y_pred


# In[100]:


x_train


# In[101]:


y_train


# In[102]:


x_test


# In[103]:


from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(x_train,y_train)


# In[105]:


y_pred=model.predict(x_test)
y_pred


# In[106]:


result=pd.DataFrame(columns=['Actual','Predicted'])
result['Actual']=y_test
result['Predicted']=y_pred

result


# In[111]:


from sklearn.metrics import *
res = r2_score(y_test,y_pred)
res*100
# how well our model is predicting the target 


# In[112]:


sns.regplot(x=y_pred,y=y_test)
plt.title('Regression Plot')
plt.xlabel('Model Prediction')
plt.ylabel('Actual Answer')
plt.show()


# In[ ]:




