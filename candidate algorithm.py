#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
play=pd.read_csv('play.csv')
play


# In[3]:


conc=np.array(play)[:,:-1]
print(conc)


# In[4]:


tar=np.array(play)[:,-1:]
print(tar)


# In[10]:


def candidate(conc, tar): 
    spec= conc[0].copy()
    print("\nSpec: ", spec)
    gen = [["?" for i in range(len(spec))] for i in range(len(spec))]
    print("\nGeneric Boundary: ",gen)
    
    for i, val in enumerate(conc):
        print("\nInstance", i+1 , "is ", val)
        if tar[i] == "yes":
            print("Instance is Positive ")
            for x in range(len(spec)): 
                if val[x]!= spec[x]:                    
                    spec[x] ='?'                     
                    gen[x][x] ='?'
                    
        if tar[i] == "no":            
            print("Instance is Negative ")
            for x in range(len(spec)): 
                if val[x]!= spec[x]:                    
                    gen[x][x] = spec[x]                              
                else:                    
                    gen[x][x] = '?' 
                    
        print("Specific Boundary after ", i+1, "Instance is ", spec)         
        print("Generic Boundary after ", i+1, "Instance is ", gen)
        print("\n")
        
        
        indices = [i for i, val in enumerate(gen) if val == ['?', '?', '?', '?', '?', '?']]    
    
    for i in indices:   
        gen.remove(['?', '?', '?', '?', '?', '?']) 
    
    return spec, gen 
s_final, g_final = candidate(conc, tar)

print("Final Specific_h: ", s_final, sep="\n")

print("Final General_h: ", g_final, sep="\n")


# In[ ]:




