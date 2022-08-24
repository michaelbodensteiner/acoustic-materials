#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
df = pd.read_html("https://www.atsacoustics.com/page--Selecting-the-Right-Acoustic-Material--ac.html")


# In[2]:


df[2]


# In[3]:


df = df[2]
df_clean = df.drop(labels=[2,3,5,6,8,9,11,12,14,15,17,18,20,21,23,24,26,27,29,30,32,33,35,36,38,39,41,42,44,45,47,48,50,51], axis = 0)


# In[4]:


df_clean.columns = df_clean.iloc[0] 
df_clean = df_clean[1:]


# In[5]:


df = df_clean.reset_index(drop=True)
df


# In[ ]:


df.to_excel("materials.xlsx")

