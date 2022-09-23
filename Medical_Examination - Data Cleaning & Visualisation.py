#!/usr/bin/env python
# coding: utf-8

# In[283]:


import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[284]:


medical_data = pd.read_csv('medical_examination.csv')


# In[285]:


medical_data.head()


# In[286]:


Height_sq= medical_data['height'].pow(2)/10000

Height_sq


# In[287]:


medical_data['Over_weight']=(medical_data['weight']/Height_sq).apply(lambda x: 1 if x > 25 else 0)
BMI_value


# In[288]:


medical_data


# In[289]:


medical_data['gluc']=medical_data['gluc'].apply(lambda y: 1 if y > 1 else 0)
medical_data['cholesterol']=medical_data['cholesterol'].apply(lambda y: 1 if y > 1 else 0)


# In[290]:


#df['cholesterol'].apply(lambda x: 0 if x == 1 else 1)


# In[291]:


medical_data


# In[292]:


medical_data_cat = pd.melt(medical_data, id_vars=['cardio'], value_vars=['active','alco','cholesterol','gluc','Over_weight','smoke'])


# In[293]:


sns.catplot(x='variable',col='cardio',hue='value',kind='count',data= medical_data_cat)


# In[294]:


medical_data_filtered = medical_data[(medical_data['ap_lo'] <= medical_data['ap_hi']) & (medical_data['height'] >= medical_data['height'].quantile(0.025)) & (medical_data['height'] < medical_data['height'].quantile(0.975)) & (medical_data['weight'] >= medical_data['weight'].quantile(0.025)) & (medical_data['weight'] < medical_data['weight'].quantile(0.975))]


# In[295]:


Corr = medical_data_filtered.corr()


# In[ ]:


mask = np.zeros_like(Corr)
mask[np.triu_indices_from(mask)] = True
with sns.axes_style("white"):
    f, fig = plt.subplots(figsize=(12, 7))
    fig = sns.heatmap(Corr,vmin=0,vmax=.25,square=True,annot=True,linewidths=.5,fmt=".1f",mask=mask)


# In[ ]:





# In[ ]:





# In[ ]:




