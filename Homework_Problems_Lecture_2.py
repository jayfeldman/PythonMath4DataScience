#!/usr/bin/env python
# coding: utf-8

# # Beginner Python and Math for Data Science
# 
# ## Lecture 2 - Homework 
# 
# ### Python's Built-in Data Types

# #### 1. Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string (Assume string is longer than 2 chars). 
# 
# Sample String : 'burger'  
# Expected Result : 'buer'  
# Sample String : 'pi'  
# Expected Result : 'pipi'

# In[1]:


# 1. Solution

string = 'burger'
#string = 'pi'

first_two_chars = string[0:2]
last_two_chars = string[-1:-3:-1]
last_two_chars = string[len(string)-2:len(string)]

#Use format() function
print("{}{}".format(first_two_chars, last_two_chars))

#Use formatted string literals
print(f"{first_two_chars}{last_two_chars}")


# #### 2. Write a Python function that checks whether a word is a palindrome without using any loops.  
# 
# Note: A palindrome is a word that reads the same backward as forward.  
# Example: level  
# 
# Hint: Remember that strings also behave like a list in Python, so you can perform list operations on strings.

# In[2]:


# 2. Solution

word = "level"
word_as_list = list(word)
word_as_list_reversed = word_as_list.copy()
word_as_list_reversed.reverse()

if word_as_list == word_as_list_reversed:
    print (word, "is a palindrome.")
else:
    print (word, "is not a palindrome.")


# #### 3. Given a dictionary, write a Python program to create a list for all the keys, and another list for all the values of the dictionary.
# 
# Example: my_dict = {"a":1, "b":2, "c":3}  
# Expected Result: l1 = ["a", "b", "c"], l2 = [1, 2, 3]

# In[3]:


# 3. Solution

my_dict = {"a":1, "b":2, "c":3}

l1 = list(my_dict.keys())
l2 = list(my_dict.values())

print(l1, '\n', l2)


# #### 4. Given a list of numbers, write a program to compute the sum of the first and last numbers of the list.

# In[15]:


# 4. Solution

list = [4, 3, 2, 5, 1, 6]

sum = list[0] + list[len(list)-1]
print(sum)


# #### 5. Write a Python program to print out a set containing all the colors from color_list_1 which are not present in color_list_2.
# 
# Test Data :  
# color_list_1 = set(["White", "Black", "Red"])   
# color_list_2 = set(["Red", "Green"])  
# Expected Output :  
# {'Black', 'White'}

# In[4]:


# 5. Solution

color_list_1 = set(["White", "Black", "Red"])   
color_list_2 = set(["Red", "Green"])

color_list_1.difference(color_list_2)


# In[ ]:




