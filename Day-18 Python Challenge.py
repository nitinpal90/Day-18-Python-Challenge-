#!/usr/bin/env python
# coding: utf-8

# # Day-18 Python Challenge

# # Seaborn library

# In[5]:


import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


# In[6]:


var = [1,2,3,4,5]
var1 = [10,20,30,40,50]


# In[7]:


plt.plot(var, var1)
plt.show()


# In[8]:


df = pd.DataFrame({"var": var, "var1": var1})
sns.lineplot(x = 'var', y = 'var1', data = df)
plt.show()


# In[31]:


df1 = sns.load_dataset("penguins")


# In[32]:


df1.head()


# In[33]:


sns.lineplot(x = "bill_length_mm", y = "flipper_length_mm", data = df1)
plt.show()


# # Categorical Function

# In[34]:


sns.lineplot(x = "bill_length_mm", y = "flipper_length_mm", data = df1, hue = "sex")
plt.show()


# # Colour Formating in Graphs

# In[35]:


sns.lineplot(x = "bill_length_mm", y = "flipper_length_mm", data = df1, hue = "sex", palette = 'rocket_r')
plt.show()


# # Marker Shapes in Graph

# In[36]:


sns.lineplot(x = "bill_length_mm", y = "flipper_length_mm", data = df1, hue = "sex", 
             palette = 'rocket_r', markers = ["o", "<"])
plt.show()


# In[39]:


df1 = sns.load_dataset("penguins").head(20)
df1


# In[41]:


sns.lineplot(x = "bill_length_mm", y = "flipper_length_mm", data = df1, hue = "sex", 
             palette = 'rocket_r')
plt.show()


# # Grid in Graphs

# In[44]:


sns.lineplot(x = "bill_length_mm", y = "flipper_length_mm", data = df1, hue = "sex", 
             palette = 'rocket_r')
plt.grid()
plt.show()


# # Title Function

# In[45]:


sns.lineplot(x = "bill_length_mm", y = "flipper_length_mm", data = df1, hue = "sex", 
             palette = 'rocket_r')
plt.grid()
plt.title("Linear Graph from Penguins Data Set")
plt.show()

