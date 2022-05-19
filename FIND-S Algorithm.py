#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
play=pd.read_csv('play.csv')


# In[2]:


play


# In[6]:


conc=np.array(play)[:,:-1]
print(conc)


# In[8]:


tar=np.array(play)[:,-1:]
print(tar)


# In[25]:


def finds(tar,conc):
    for i ,val in enumerate(tar):
        if val=='yes':
            spec=conc[i].copy()
        break;
    for i,val in enumerate(conc):
        if tar[i]=='yes':
            for x in range (len(spec)):
                if val[x]!=spec[x]:
                    spec[x]='?'
                else:
                        pass
        print( "hypothesis",i)
        print(spec)
    
print('The maximal specific hypothesis is')
            
print(finds(tar,conc))
        


# In[ ]:




