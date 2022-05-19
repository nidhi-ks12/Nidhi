#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
d=pd.read_csv('diabetes.csv')


# In[2]:


print(d)


# In[4]:


d.isnull().sum()


# In[5]:


d.describe()


# In[6]:


d.std()


# In[7]:


d.var()


# In[8]:


d.head()


# In[9]:


d['Pregnancies'].hist()


# In[10]:


d.median()


# In[11]:


d.plot(x='Glucose', y='BMI',kind='box')


# In[15]:


d1=pd.read_excel('d.xlsx')


# In[16]:


print(d1)


# In[17]:


d1.isnull().sum()


# In[18]:


d2=pd.read_csv('d2.csv')


# In[19]:


d2.isnull().sum()


# In[20]:


d2.tail()


# In[44]:


n = pd.read_csv('d2.csv', index_col=0 , na_values=["??","##"])


# In[45]:


n.isnull().sum()


# In[46]:


n.describe()


# In[24]:


n.var()


# In[25]:


n.median()


# In[56]:


n["Age"]=n["Age"].replace(np.NaN,n["Age"].mean())


# In[27]:


n.head()


# In[49]:


n["Outcome"]= n["Outcome"].replace(np.NaN,n["Outcome"].mean())


# In[50]:


n["DiabetesPedigreeFunction"]= n["DiabetesPedigreeFunction"].replace(np.NaN,n["DiabetesPedigreeFunction"].mean())


# In[51]:


n["Insulin"]= n["Insulin"].replace(np.NaN,n["Insulin"].mean())


# In[52]:


n["SkinThickness"]= n["SkinThickness"].replace(np.NaN,n["SkinThickness"].mean())


# In[53]:


n["Glucose"]= n["Glucose"].replace(np.NaN,n["Glucose"].mean())


# In[57]:


n.isnull().sum()


# In[55]:


n['Glucose'].mean()


# In[58]:


n.plot(x='Age', y='Outcome',kind='box')


# In[59]:


n.plot(x='Age', y='Glucose',kind='box')


# In[60]:


n.plot(x='Age', y='BloodPressure',kind='box')


# In[61]:


n.plot(x='Age', y='Glucose',kind='scatter')


# In[62]:


n.plot(x='Age', y='BloodPressure',kind='scatter')


# In[63]:


n.plot(x='Age', y='Outcome',kind='scatter')


# In[64]:


n['Outcome'].unique()


# In[ ]:




