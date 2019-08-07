#!/usr/bin/env python
# coding: utf-8

# # Beginner Python and Math for Data Science
# 
# ## Lecture 3 - Homework
# 
# ### If Statements, Loops, Functions

# In[3]:


# example of a function

def function1(input1):
    # do something
    output = input1/2
    return output


# #### 1. Write a function that takes in a list as input and returns a new list with only the even integers from that list.
# 
# Sample input: [1,4,5,11,12,15]  
# Expected output: [4,12]

# In[1]:


# 1. Solution

def even_int(inp_list):
    # your solution here
    int_list = []
    for i in inp_list:
        if i%2 == 0:
            int_list += [i]
    return int_list

# Testcases
even_int([1,4,5,11,12,15])


# #### 2. You are given a dictionary that has the count of the number of each fruit in a basket. Write a function that takes in the dictionary and outputs the total number of fruits in the basket.
# 
# Sample input: fruits = {"oranges": 5, "apples": 2, "blueberries": 12}
# Expected output: 19

# In[2]:


# 2. Solution

def count_fruits(fruits):
    pieces_of_fruit = int()
    
    for value in fruits.values():
        pieces_of_fruit += value
    return print("There are", pieces_of_fruit, "pieces of fruit in total.")

# Testcases
fruits = {"oranges": 5, "apples": 2, "blueberries": 12}
count_fruits(fruits)


# #### 3. Write a Python program that accepts a string and calculate the number of digits and letters. 
# 
# Sample Data : Python 3.2  
# 
# Expected Output :  
# Letters 6  
# Digits 2  
# 
# Hint: Make use of Python string's inherent isdigit() method and isalpha() method. For example, "a".isdigit() returns False, while "a".isalpha() returns True.

# In[3]:


# 3. Solution

def letters_digits(s):
    Letters = int()
    Digits = int()
    
    for char in s:
        if char.isdigit():
            Digits += 1
        elif char.isalpha():
            Letters += 1

    return print("Letters", Letters, "\nDigits", Digits)

# Testcases
letters_digits("Python 3.2")


# #### 4. Write a Python program to check the validity of a password.
# 
# Validation :  
# At least 1 character from [$#@].  
# Minimum length 6 characters.  
# Maximum length 16 characters.  

# In[5]:


# 4. Solution

def valid_password(p):
    import string
    contains_special_char = bool()
    validation = str()

    for s in p:
        if s in string.punctuation:
            contains_special_char = bool(True)
    if not contains_special_char:
        validation = print("{} does not contain a special character".format(p))
    elif  len(p) >= 6 and len(p) <= 16:
        validation = print("{} is a valid password.".format(p))
    else:
        validation = print("{} is not between 6 and 16 characters.".format(p))
    return validation

# Testcases
valid_password("135oijafea$f") # should return True, length between 6-16, contains special char
valid_password("13oir31noaef") # should return False, does not contain special char
valid_password("$13oir31noaefapeofdfdsffsdfsd") # should return False, too long
valid_password("$13sd") # should return False, too short


# #### 5. Write a function that takes in a number between 1 and 50 as input, and guesses the correct number in least number of tries. You should print the number of guesses it took to correctly find the number.
# 
# You can import the random module to guess random numbers, or you can think of a more efficient way to guess the correct number in the least number of guesses.

# In[8]:


# 5. Solution

#import random

#Uses recursive binary search to find num between lower and upper limits
def guess_num(num, lower, upper, attempt):
    result = ""
    mid = int((lower + upper) / 2); 
    print("lower = {} mid = {} upper = {}".format(lower, mid, upper))
    
    if num == mid:
        result = print("It took {} attempt(s) to guess {}".format(attempt,num))
    elif num > mid:
        print("{} is greater than {}".format(num, mid))
        attempt += 1
        lower = mid+1
        guess_num(num, lower, upper, attempt)
    else:
        print("{} is less than {}".format(num, mid))
        attempt += 1
        upper = mid-1
        guess_num(num, lower, upper, attempt)
    return result

# Testcases
guess_num(20, 1, 50, 1)


# In[ ]:




