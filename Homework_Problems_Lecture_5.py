#!/usr/bin/env python
# coding: utf-8

# # Beginner Python and Math for Data Science
# 
# ## Lecture 5 - Homework
# 
# ### Intro to Pandas

# In[5]:


from IPython.display import Image
import pandas as pd


# In[6]:


Image(filename = "df.png")


# #### Create a dataframe for the shopping list, with color and count for each item in the basket (your output should match the picture above). Assign this dataframe to a new variable named `shopping_cart `, and display the first two rows of this dataframe.

# In[67]:


# Solution

my_list = [{"Color":"Red","Count" : 2},
           {"Color":"Green", "Count": 5},
           {"Color":"Orange", "Count" : 3}]

shopping_cart = pd.DataFrame(my_list, index = ["Apple", "Kale", "Carrots"])

shopping_cart


# #### Select the Color column in the shopping_cart dataframe and assign the resulting series to a new variable `Color`.

# In[66]:


# Solution

Color = shopping_cart["Color"]

print(Color, "\n")

print(type(Color))


# #### For the Color series created above, return a new boolean array that returns true if the color is either Red or Orange.

# In[65]:


# Solution 

my_bool = list(map(lambda x : x in ("Red", "Orange"), Color))

print(my_bool, "\n")

shopping_cart[my_bool]


# #### In the dataframe `shopping_cart`, select only the items with count greater or equal to 3 using Boolean indexing.
# 
# Note: Kale and carrots should be shown.

# In[64]:


# Solution

shopping_cart[shopping_cart["Count"] >= 3]


# #### Find the number of apples in the baskets in the dataframe using loc and iloc. 
# Note: should be 2

# In[62]:


# Solution using loc

print(shopping_cart, "\n")

shopping_cart.loc["Apple", "Count"]


# In[63]:


# Solution using iloc

print(shopping_cart.iloc[0,1])


# In[ ]:




