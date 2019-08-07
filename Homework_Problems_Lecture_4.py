#!/usr/bin/env python
# coding: utf-8

# # Beginner Python and Math for Data Science
# 
# ## Lecture 4 - Homework
# 
# ### Advanced Beginner Concepts of Python and Introduction to Numpy

# #### 1. Last homework, we wrote a function that takes in a list as input and returns a new list with only the even integers from that list. Write a version 2 of the function that does the same thing, but using a one-line list comprehension.
# 
# Sample input: [1,4,5,11,12,15]  
# Expected output: [4,12]

# In[63]:


def even_int(inp_list):
    out_list = []
    for i in inp_list:
        if i % 2 == 0:
            out_list.append(i)
    return out_list


# Testcases
inp_list = [1,4,5,11,12,15]
even_int([1,4,5,11,12,15])


# In[73]:


# 1. Solution

def even_int2(inp_list):
    even_values = [vals for vals in inp_list if vals % 2 == 0]
    return even_values

# Test cases
even_int2([1,4,5,11,12,15])


# #### 2. Write a function that takes a list as input and returns a product of all the elements in the list. Use Python's reduce function.
# 
# Sample input: [1,2,3]  
# Expected output: 6

# In[72]:


# 2. Solution

from functools import reduce

def product(inp_list):
    product_of_elements = reduce(lambda v1, v2 : v1*v2 , inp_list)
    return product_of_elements

# Testcases
inp = [1,2,3,4]
product(inp)


# #### 3. In the last homework, we wrote a Python program that accepts a string and calculate the number of digits and letters (if you haven't already, go try this problem first). Below is a slightly modified version that returns a tuple of letters and digits. Given a list of strings, apply this function to return a new list with the tuples of letters and digits.
# 
# Sample Data : ["Python 3.2", "abc92", "qwerty"]  
# 
# Expected Output :  
# [(6, 2), (3,2), (6,0)]  
# *_ because there are 6 letters and 2 digits in the Python 3.2, etc. _*  

# In[71]:


# 3. Solution

def letters_digits(s):
    """
    Given a string, returns a tuple (number of letters, number of digits)
    """
    d=l=0
    for c in s:
        if c.isdigit():
            d=d+1
        elif c.isalpha():
            l=l+1
    return (l, d)

def letters_digits_list(s_list):
    new_list = list(map(letters_digits, s_list))
    return new_list

letters_digits_list(["Python 3.2", "abc92", "qwerty"] )


# #### 4. Given a list of passwords and a function that checks the validity of a password, write a function that returns how many of the passwords in the list is valid. (Try without using a for loop)
# 
# Validation :  
# At least 1 character from [$#@].  
# Minimum length 6 characters.  
# Maximum length 16 characters.  
# 
# Sample: ["valid$password", "#valid_password", "not_valid"]  
# expected: 2

# In[70]:


# 4. Solution

def valid_password(p):
    if (len(p) < 6) or (len(p) > 16):
        return False
    special = "$#@"
    for char in p:
        if char in special:
            return True
    return False


def num_valid_passwords(pass_list):
    count = sum(map(valid_password, pass_list))
    return count

num_valid_passwords(["valid$password", "#valid_password", "not_valid", "not_validpassword"]) # should return 2


# #### 5. Create a numpy array of zeros that has 5 rows and 2 columns. Then stack the given array vertically s.t. the given array is at the top row of the new array.

# In[69]:


# 5. Solution

import numpy as np

arr = np.array([1,2]) # stack this array s.t. this array is at the top. Resulting array should be of size (6,2)
#print(arr)

arr_2 = np.zeros([5,2], dtype=int)

arr_3 = np.vstack([arr, arr_2])
print(arr_3)


# In[ ]:




