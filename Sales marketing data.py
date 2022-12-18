#!/usr/bin/env python
# coding: utf-8

# In[113]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[114]:


sales = pd.read_excel("supermarket.xls")


# In[115]:


sales


# In[116]:


sales.head()


# In[117]:


sales.tail()


# In[118]:


sales.dtypes


# In[119]:


type(sales['Date'][0])


# In[120]:


from pandas import to_datetime


# In[121]:


sales['Date']=to_datetime(sales['Date'])


# In[122]:


type(sales['Date'][0])


# In[123]:


sales['Date'].dtype


# In[124]:


type(sales['Time'][0])


# In[125]:


sales['Date']


# In[126]:


sales['Time']


# In[127]:


def fetch_att(x):
    day=x.day
    month=x.month
    year=x.year
    return pd.Series([day,month,year])


# In[128]:


sales[['day','month','year']]=sales['Date'].apply(fetch_att)


# In[129]:


sales.head()


# In[130]:


sales['Date'].apply(lambda x:x.day)


# In[131]:


sales['Date'].dt.year


# In[132]:


sales.columns


# In[133]:


sales['hour']=sales['Time'].apply(lambda x:x.hour)


# In[134]:


sales.head()


# In[135]:


sales['Time']


# In[136]:


sales.describe().T


# In[137]:


sales.corr()


# In[138]:


np.round(sales.corr(),2)


# In[139]:


plt.figure(figsize=(14,8))
sns.heatmap(np.round(sales.corr(),2),annot=True)


# In[140]:


sns.scatterplot(x='Tax 5%',y='gross income',data=sales)


# In[141]:


sns.scatterplot(x='Quantity',y='cogs',data=sales,color='green')


# In[142]:


sns.regplot(x='Quantity',y='cogs',data=sales,color='green')


# In[143]:


sales['City'].unique()


# In[144]:


sales.groupby(['City'])['gross income'].median()


# In[145]:


sales['Rating'].mean()


# In[146]:


sns.displot(sales['Rating'],kde=False)
plt.axvline(x=np.mean(sales['Rating']),c='red',label='Avg Rating')


# In[147]:


def return_countplot(column,hue_name=None):
    return sns.countplot(x=column,data=sales,hue=hue_name)    


# In[148]:


def return_boxplot(x_column,y_column):
    return sns.boxplot(x=x_column,y=y_column,data=sales)


# In[149]:


def return_lineplot(x_column,y_column):
    return sns.lineplot(x=x_column,y=y_column,data=sales)


# In[150]:


def return_rel_plot(x_col, y_col, col_name=None, row_name=None, rel_type=None, hue_name=None, style_name=None):
    return sns.relplot(x=x_col, y=y_col, col=col_name, row=row_name, kind=rel_type, hue=hue_name, style=style_name, data=sales)


# In[151]:


return_boxplot('Branch','Rating')


# In[155]:


sales.columns


# In[156]:


sales.dtypes


# In[157]:


return_lineplot('hour','Quantity')


# In[158]:


return_rel_plot(x_col='hour',y_col='Quantity',col_name='month',row_name='Branch',rel_type='line',hue_name='Gender',style_name='Gender')


# In[159]:


return_rel_plot(x_col='hour',y_col='Total',col_name='month',row_name='Branch',rel_type='line')


# In[162]:


return_rel_plot(x_col='hour',y_col='Total',col_name='Product line',row_name='Branch',rel_type='line')


# In[163]:


return_boxplot('Quantity','Product line')


# In[166]:


plt.figure(figsize=(14,8))
return_countplot('Product line')


# In[167]:


return_rel_plot('gross income','Product line',rel_type='scatter')


# In[168]:


return_countplot('Payment',hue_name='Branch')


# In[172]:


sales.groupby('Customer_type')['Total'].sum()


# In[174]:


sales.groupby('Customer_type').agg({'Total':'sum'})


# In[176]:


sns.swarmplot(x='Customer_type',y='Rating',data=sales,hue='City')


# In[ ]:




