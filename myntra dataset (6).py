#!/usr/bin/env python
# coding: utf-8

# ### INT353 CA-2
# #### Name - Aman Gautam
# #### Registration number - 12016284
# #### Roll no- RK20RUA20
# 

# #### PROJECT - Myntra Fasion Clothing
# 

# ## INTRODUCTION-
# 
# 
# #### Myntra is a popular name among fashion enthusiasts, by fashion enthusiasts we mean quite everyone. Everyone wants to make a style statement, and everyone wants to stand out. In this sort of environment, Myntra is a perfect destination for these people. It is a place that caters to a lot of demands in a single and simple setting. A single stop for all things fashion.
# 

# ## Why I chose Myntra Fashion-
# 
# #### In this dataset I analysis the trends of different products according to reviews and ratings according to different categories and brands. I will also remove the different outliers and null values which affect the data.This dataset has   526564 rows and 13columns
# 

# ### The columns in the dataset are described as follows:
# #### 1.	URL of the Product – It has the URL of all product list present in dataset.
# #### 2.	Productid – It has the id of all product present in dataset and each value ahs its own unique id so that that no two products have similar id
# #### 3.	Brand Name- it contains all top brand names whose products are sell by Myntra online.
# #### 4.	Category – It contains all categories of clothes whether its western, Indian and other categories.
# #### 5.	Individual category – It contains all individual details like whether its shirt, pants or any other women wear.
# #### 6.	Category by gender – It tells whether the products is for women or men.
# #### 7.	Description – It tells a detailed description of the product with information about the clothes so that user can think about it before it.
# #### 8.	Discount price – It shows the product price after the discount amount is reduced from the main price.
# #### 9.	Original price – It shows the original price without reducing the discount price from data.
# #### 10.	Discount – The column shows the discount percent of all the products that how much discount is present in data.
# #### 11.	Size- It shows how many different sizes of a product is available in store.
# #### 12.	Ratings – it shows the ratings of a product given by users to the product.
# #### 13.	Reviews - It shows the total reviews shown by different buyers after buying the product from Myntra
# 

# #### --------------------------------------------------------------------------------------

# ### ->FIRST WE IMPORT DIFFERENT PYTHON LIBRARIES WHICH WE WILL USE IN OUR PROJECT

# In[7]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")


# ### ->IMPORTING THE EXCEL FILE DATA

# In[8]:


data=pd.read_csv("Myntra Fasion Clothing.csv")


# In[9]:


#pd.set_option("display.max_rows", None, "display.max_columns", None)


# In[10]:


data.head()


# ### ->First we change the column order as we need to check the product_id first then at the end we need to see URL of the product which makes the dataset easy to read
# 

# In[11]:


data.head()


# ### *------------------*---------------------------*

# ### ->Getting dimension or shape of dataset

# In[12]:


data.shape


# ### ->Using pandas info() to find the non-null values and data types of different columns

# In[13]:


data.info()


# 
# ### This dataset contains float, int, object values

# ### ----------------------------------------

# ### ->Using pandas .isnull().sum()  to get the count of sum of all null values present oin 

# In[14]:


data.isnull().sum() 


# In[ ]:





# ### -> There are 4 columns with  null values i.e.
# 1. DiscountPrice (in Rs)   - 193158
# 2. DiscountOffer           -  74306
# 3. Ratings                 - 336152
# 4. Reviews                 - 336152

# # DATA CLEANING

# ### ->As we know that the first column with null values is "DiscountPrice (in Rs)" 

# ### ->Getting the counts of each value present in the "DiscountPrice (in Rs)" column using pandas .value_counts()

# In[15]:


data["DiscountPrice (in Rs)"].value_counts()


# In[16]:


## Getting the statistical values of column 'DiscountPrice (in Rs)' using describe() funtion
data['DiscountPrice (in Rs)'].describe()


# ### ->As we can see there is lot of variations min max value so we can"t use any statistical value directly related to this columns

# #### we can use  price values related to different categories 

# In[17]:


data['Category'].value_counts()


# ## ->Using groupby to get the mean of different discount price according to diffrent category

# In[18]:


data.groupby('Category').mean()['DiscountPrice (in Rs)']


# ### ->in the following method, we have used groupby() and transform() functions to replace the mean of different  Null values.
# 

# In[19]:


data['DiscountPrice (in Rs)'] = data['DiscountPrice (in Rs)'].fillna(data.groupby('Category')['DiscountPrice (in Rs)'].transform('mean'))


# In[20]:


data['DiscountPrice (in Rs)'].describe() 


# ### Conclusion
# #### As we can see there is not that much change in statistical values because we add mean values according to different categories 

# In[21]:


data.isnull().sum() # now we succefully remove the null values of this column


# ### conclusion 
# #### the null values of the column 'DiscountPrice (in Rs)' is seccessfully removed
# 

# ###  --------                     ----------------------                                --------------------

# ## CLEANING NULL VALUES OF COLUMN 'Ratings'

# In[22]:


data['Ratings'].value_counts()


# In[23]:


data['Ratings'].describe() # we can't use mean value in null values here because mean is close to max value which is not a good odea to use in this 


# #### By checking the statistical values we see we can't use mean value in null values here because mean is close to max value which is not a good 

# In[24]:


data.groupby('Category').mean()['Ratings'] 


# ### -> we can't use mean according to each category so we have to drop this idea too

# ### ------Lets find the mean of rating with respect to the 'Individual_category'-----

# In[25]:


data.groupby('Individual_category').mean()['Ratings']


# ### ->Conclusion
# #### As we can see the variation of mean using the individual category is a good idea 
# #### But there are also some null values whose mean is not shown because of less value counts so we ahve to remove those numbers

# In[26]:


data['Individual_category'].value_counts()


# ####  Removing the Individual category data with less value counts

# In[27]:


counts = data['Individual_category'].value_counts()

data = data[~data['Individual_category'].isin(counts[counts < 11].index)]


# In[28]:


data['Individual_category'].value_counts()


# In[29]:


data.groupby('Individual_category').mean()['Ratings'] 


# In[30]:


data["Ratings"].describe()


# ### -> As we can see the statistical values of the ratings does not changed after removing some data of individual category

# ### Filling the Average values in null values in 'Ratings' columns with respect to the 'Individual_category' columns

# In[31]:


data['Ratings'] = data['Ratings'].fillna(data.groupby('Individual_category')['Ratings'].transform('mean'))


# In[32]:


data["Ratings"].describe() 


# ## Colnclusion
# ### So after filling the null values there is not much change in statistcial data

# ## -------------------------------------------------------------------------

# ### ->Cleaning null values from the column 'DiscountPrice (in Rs)'

# In[33]:


data["DiscountPrice (in Rs)"].isnull().sum()


# #### ->statisticsl values of column

# In[34]:


data["DiscountPrice (in Rs)"].describe()


# ### ->Filling the Average values in null values in 'DiscountPrice (in Rs)' columns with respect to the 'Individual_category' columns

# In[35]:


data['DiscountPrice (in Rs)'] = data['DiscountPrice (in Rs)'].fillna(data.groupby('Individual_category')['DiscountPrice (in Rs)'].transform('mean'))


# In[36]:


data['DiscountPrice (in Rs)'].isnull().sum()


# ### Removing the remaining null values

# In[37]:


data.dropna(subset=['DiscountPrice (in Rs)'], inplace=True)


# In[38]:


data['DiscountPrice (in Rs)'].isnull().sum()


# ### ---------------------------------------------------

# ## ->Cleaning null values from the column 'DiscountOffer'

# In[39]:


data.isnull().sum() 


# ### First we have to convert column datatype into Integer
# ### we have to change the discount price missing values according to discount offer 

# In[40]:


#data["DiscountOffer)"]=data["DiscountOffer"].str.replace(" OFF","% OFF")
data["DiscountOffer"]=data["DiscountOffer"].str.replace('[OFF,"OFF",Hurry*,' ',"%","Rs. "]', '')


# In[41]:


data["DiscountOffer"].value_counts()


# In[42]:


data['DiscountOffer'] = data['DiscountOffer'].fillna(0)


# ### Conclusion
# #### We fill the null values as 0 because there is no discount on those products

# In[43]:


data["DiscountOffer"].isnull().sum()


# ### ------------------------------------------------------------

# ## ->Cleaning null values from the column "Reviews"

# In[44]:


data["Reviews"].value_counts().head()


# ### As we can see it contains large number of null values with different variations and a gerat difference in min and max value

# In[45]:


data.groupby('Individual_category').mean()['Reviews'] 


# In[46]:


data['Reviews'].describe()


# ### We can use forward and backword fill in reviews as in many cases the forwrd and backword values are same

# In[47]:


data['Reviews'] = data['Reviews'].fillna(method="ffill")
#data['Reviews'] = data['Reviews'].interpolate()


# ### we are getting the same result as using the .interpolate() method which is use to guess the missing values in data
# 

# In[48]:


data['Reviews'].describe()


# In[49]:


data.isnull().sum()


# ### ----------------------------------------------------------

# ## UNIVARIATE ANALYSIS

# In[50]:


data.head()


# In[51]:


ax=plt.figure(figsize=[8,6])
explode = (0.1, 0)
data["category_by_Gender"].value_counts().plot.pie(explode=explode,autopct = "%.2f%%", shadow=True,colors = ['blue', 'yellow'],startangle=90)
plt.legend()


# ## Conclusion
# ### This graph shows the difference in male and female products using bar graph

# In[52]:





ax=plt.figure(figsize=[8,6])
data["Category"].value_counts().plot.barh(color='blue',edgecolor='red')
plt.legend()


# ## Conclusion
# ### This graph shows the difference in Category of different products using bar graph

# In[53]:


ax=plt.figure(figsize=[8,6])
data["BrandName"].value_counts().head(10).plot.barh(50,200,color='yellow',edgecolor='blue')
plt.legend()


# ## Conclusion
# ### This graph shows the TOP -10 product brand using bar graph
# 

# In[54]:


ax=plt.figure(figsize=[18,16])
data["Individual_category"].value_counts().plot.barh(color='green',edgecolor='red')
plt.legend()


# ## Conclusion
# ### This graph shows the TOP-20 product brand using bar graph
# 

# In[55]:


ax=plt.figure(figsize=[18,6])
data.Ratings.plot.hist(bins=40)
plt.show()


# ## Conclusion
# ### This graph shows the where the most ratings area of products using histogram4
# ### lie in 3.5 - 4.5

# # Bivariate Analysis

# In[56]:


data.head()


# In[57]:


ax=plt.figure(figsize=[8,6])
data.groupby('Category').mean()['DiscountPrice (in Rs)'].head(15).plot.barh(color='green',edgecolor='red')
plt.legend()


# ## Conclusion
# ### It shows the mean discount on each category
# ### it is found that western wear has high mean descount price

# In[58]:


ax=plt.figure(figsize=[16,20])
data.groupby('Individual_category').mean()['DiscountPrice (in Rs)'].plot.barh(color='green',edgecolor='red')
plt.legend()


# ## Conclusion
# ### It shows the mean discount of all individual clothes
# ### it is found that suits ahev high discount price

# In[59]:


ax=plt.figure(figsize=[10,6])
data.groupby('Category').mean()['OriginalPrice (in Rs)'].plot.barh(color='blue',edgecolor='red')
plt.legend()


# ## Conclusion
# ### It shows the mean price of all individual category of clothes
# ### it is found that the indian wear has high mean price on myntra

# In[60]:


ax=plt.figure(figsize=[16,20])
data.groupby('Individual_category').mean()['OriginalPrice (in Rs)'].plot.barh(color='blue',edgecolor='red')
plt.legend()


# ## Conclusion
# ### It shows the mean price of all individual clothes
# ### it is found that suits are most expnesive average price on myntra platform

# In[61]:


data.corr()


# In[62]:


# displaying the plotted heatmap
ax=plt.figure(figsize=[9,7])
sns.heatmap(data = data.corr(),cmap="Blues",annot=True) 
plt.show()


# ## Conclusion
# ### this heatmap shows the realtionship of data as using correaltion 

# In[63]:


### Multivariate


# In[82]:


data.head()


# In[83]:


# Lets compare top 3 brand Pothys, kalini, roadster
data_Roadster=data.loc[data["BrandName"]=="Roadster"]
data_Pothys=data.loc[data["BrandName"]=="Pothys"]
data_KALINI=data.loc[data["BrandName"]=="KALINI"]


# In[87]:


plt.plot(data_Roadster["Reviews"],np.zeros_like(data_Roadster["Reviews"]),'o')
plt.plot(data_Pothys["Reviews"],np.zeros_like(data_Pothys["Reviews"]),'o')
plt.plot(data_KALINI["Reviews"],np.zeros_like(data_KALINI["Reviews"]),'o')
plt.show()


# In[ ]:




