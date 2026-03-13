#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[4]:


df=pd.read_csv("heart (1) (1).csv")
df


# ***age :*** age of the patient.
# 
# ***sex :*** gender of the person (0-female and 1-male ).
# 
# ***cp  :*** chest pain of the patient.
# 
# ***testbps :*** blood pressure level at the resting condition.
# 
# ***chol :*** cholestrol level at admission at hospital.
# 
# ***fbs :*** fasting blood sugar level of the patient.
# 
# ***restecg :*** ECG (electro cardio graphic) level at resting condition.
# 
# ***thalach :*** maximum heart rate achieved during the test.
# 
# ***exang :*** exercise induce argina(facing any discomfort or not).
# 
# ***oldpeak :***how much ecg changes during exercise from resting.
# 
# ***slope :*** slope of the ECG.
# 
# ***ca(coronary artery) :*** the number of blood vessel covered by fluroscopy .
# 
# ***thal(thalasemia) :*** a blood disorder that can damage your heart.
# 
# ***target*** : whether a person has any heart disease or not , 1-yes 0-no.

# # EDA

# In[5]:


df.info()


# In[6]:


# check in the target column that how many patient have heart disease or how many patient dont have any heart disease
df['target'].value_counts()
# 1- means  yes heart disease , 0 - means no heart disease.


# In[7]:


# # data cleaning
# 1. check for the null value .
# 2. check for the duplicates.
# 3. check for outlier.


# In[8]:


# check for the null value 
# to drop - df.dropna(inplace=True)
df.isnull().sum().sum()


# In[9]:


#check for the duplicates
df.duplicated().sum()


# In[10]:


# drop duplicates
df.drop_duplicates(inplace=True)


# In[11]:


#check for the outliers 
for i in df.columns:
    if df[i].dtype!='object':
        plt.boxplot(df[i])
        plt.xlabel(i)
        plt.show()



# In[12]:


# as the dataset is a real patient information so we are not going to remove the outlier in that case

# and 

# as a tree algorithm dont have much effect of outliers  , then we can skip the outlier removal part 


# # MODEL BUILDING 

# In[13]:


# divide the data based on dependent and independent variable


# In[14]:


x=df.iloc[:,:-1]
y=df.iloc[:,-1]


# In[15]:


x


# In[16]:


y


# In[17]:


from sklearn.model_selection import train_test_split


# In[18]:


x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.20,random_state=40)


# In[19]:


x_train # training question


# In[20]:


y_test # training answer


# In[21]:


x_test #testing question


# In[22]:


y_test # testing answer


# In[23]:


from sklearn.tree import DecisionTreeClassifier


# In[24]:


dt=DecisionTreeClassifier()


# In[25]:


# train the model 
dt.fit(x_train,y_train)


# In[26]:


#test the model
y_pred=dt.predict(x_test)


# In[27]:


new_df=pd.DataFrame()
new_df['Actual value']=y_test
new_df['predicted value']=y_pred
new_df


# In[28]:


from sklearn.metrics import *
accuracy_score(y_test,y_pred)


# In[29]:


confusion_matrix(y_test,y_pred)


# In[30]:


from sklearn import tree


# In[31]:


tree.plot_tree(dt,fontsize=7)


# In[32]:


dt.get_depth()


# # MAX DEPTH
# max depth is a hyperparameter used in decision tree . it control how deep the tree can split the data.

# In[33]:


depth =[1,2,3,4,5,6,7,8,9,10,11,12,13]
for i in depth:
    dt=DecisionTreeClassifier(max_depth=i,random_state=42)
    dt.fit(x_train,y_train)
    y_pred=dt.predict(x_test)
    acc=accuracy_score(y_test,y_pred)
    print(f" max depth is : {i} and accuracy score is : {acc}")


# In[ ]:




