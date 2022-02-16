#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt


# In[5]:


dataset = pd.read_csv('C:\\Users\CoolT\Documents\Jupyternotebook3\WhiteAwayCase\Data\data.csv')


# In[6]:


dataset


# In[7]:


dataset['InvoiceNo'].min()
dataset['InvoiceNo'].max()


# In[15]:


unique_invoices = pd.unique(dataset['InvoiceNo'])
unique_stockcodes = pd.unique(dataset['StockCode'])


# In[19]:


print(len(unique_invoices))
print(len(unique_stockcodes))
print(len(dataset))
a = []


# In[22]:


#'71053' indices
index = dataset.index
indices_stock = index[dataset['StockCode'] == '71053']

stock_list = indices_stock.tolist()         #Giver en liste med index hvor specifikt item indgår


# In[25]:


invoice_numbers = dataset['InvoiceNo'][stock_list]        
print(invoice_numbers)
#Giver liste med de tilhørende invoice numre til de index hvor specifikt item indgår


# In[39]:


index2 = dataset.index

indices_recommend_items = index[dataset['InvoiceNo'].isin(invoice_numbers)]

recommend_count_indices = indices_recommend_items.tolist()  
#Giver liste med index til de invoices hvor specifikt item indgår, flere index til samme invoice pga de fylder flere linjer


# In[41]:


print(np.shape(recommend_count_indices))


# In[42]:


recommend_count_list = dataset['StockCode'][recommend_count_indices] 
#laver en liste med alle de stockscodes fra de tilhørende invoices


# In[43]:


print(recommend_count_list)


# In[ ]:





# In[44]:


#unique_invoices = pd.unique(dataset['InvoiceNo'])
unique_stockcode_in_invoice = pd.unique(recommend_count_list)
#Laver en liste med unikke ting der er købt sammen med det første specificerede item


# In[47]:


from collections import Counter
occurrences = Counter(recommend_count_list)
#Tæller sammen i en dictionary hvor mange der er af hver unik indgang


# In[51]:


print(occurrences)
#Den første er det specifikke item selv, så den skal der ses bortfra. De andre er de recommende items.


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




        


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




