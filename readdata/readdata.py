#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib

# In[2]:




# In[3]:


df = pd.read_csv("ML-EMHYY.csv")


# In[4]:


df.head()


# In[5]:


def arrange_time_dataframe(df):
    df.columns = ['date', 'value']
    df.sort_values(by='date', inplace=True)
    df.set_index('date', inplace=True)
    return df


# In[6]:


df = arrange_time_dataframe(df)


# In[7]:


df.head()


# In[8]:


df.plot(figsize=(16, 6))


# In[ ]:
