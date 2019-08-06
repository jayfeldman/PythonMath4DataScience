#!/usr/bin/env python
# coding: utf-8

# # Beginner Python and Math for Data Science
# 
# ## Lecture 1 - Homework 
# 
# ### Python Variables, Assignments, Comparisons and Other Basics

# #### 1. Write a Python program to convert degree to radian.
# 
# Note : The radian is the standard unit of angular measure, used in many areas of mathematics. An angle's measurement in radians is numerically equal to the length of a corresponding arc of a unit circle; one radian is just under 57.3 degrees (when the arc length is equal to the radius).
# 
# Test your solution by using `180 degrees`.

# In[1]:


"""
1. Write a Python program to convert degree to radian. Note : The radian is the standard 
unit of angular measure, used in many areas of mathematics. An angle's measurement in 
radians is numerically equal to the length of a corresponding arc of a unit circle; one 
radian is just under 57.3 degrees (when the arc length is equal to the radius).

Test your solution by using 180 degrees.
"""

import math

degree = 1
radian = degree *  math.pi/180 

print(degree, "degree(s) equals ", radian, "radians")


# #### 2. Write a Python program to calculate surface volume and area of a sphere. 
# 
# Note: A sphere is a perfectly round geometrical object in three-dimensional space that is the surface of a completely round ball.
# 
# Test your solution by using a sphere with `radius = 18`

# In[2]:


"""
2. Write a Python program to calculate surface volume and area of a sphere.¶
Note: A sphere is a perfectly round geometrical object in three-dimensional 
space that is the surface of a completely round ball.

Test your solution by using a sphere with radius = 18
"""

radius = 18
surface_area = 4 * math.pi * radius**2
volume = 4/3 * math.pi * radius**3

print("Surface Area of a Sphere with radius of", radius, "equals", round(surface_area, 2))
print("Volume of a Sphere with radius of", radius, "equals", round(volume, 2))


# #### 3. Write a Python program to solve $(x + y)(x + y)$. 
# 
# Test your solution if `x = 5` and `y = 1`

# In[3]:


"""
3. Write a Python program to solve  (𝑥+𝑦)(𝑥+𝑦) .¶

Test your solution if x = 5 and y = 1
"""
x=5
y=1

z1 = (x+y)*(x+y)
z2 = (x+y)**2
z3 = x**2 + 2*x*y + y**2

print(z1, z2, z3)


# #### 4. Write a Python program to create all possible 2-letter strings by using 'a', 'e', 'i', 'o', 'u'. 

# In[4]:


#3. Write a Python program to solve  (𝑥+𝑦)(𝑥+𝑦) .¶

# Test your solution if x = 5 and y = 1


#Given five letters, choose 2. Assume without replacement
order_matters = True
#order_matters = False
vowels = ['a', 'e', 'i', 'o', 'u']
cnt = 0

if order_matters:
    for i in vowels:
        for j in vowels:
            if i != j: 
                print(i+j)
else:
    for i in vowels:
        cnt += 1
        for j in vowels[cnt:len(vowels)]:
            if(i != j):
                print(i+j)


# #### 5. Write a Python program to test whether a number is within 100 of 1000 or 2000.
# 
# Test your solution with the number `2200`, `900`, and `800`

# In[6]:


"""
5. Write a Python program to test whether a number is within 100 of 1000 or 2000.

Test your solution with the number 2200, 900, and 800
"""

target1 = 1000
target2 = 2000

values = ['2200', '900', '2100']

for i in values:
    test_target1 = abs(target1 - int(i)) <= 100
    test_target2 = abs(target2 - int(i)) <= 100

    if(not(test_target1) and not(test_target2)):
        print(i, 'is not within 100 of', target1, 'or', target2)
    elif(test_target1 and test_target2):
        print(i, 'is within 100 of', target1, 'and', target2)
    elif(test_target1):
        print(i, 'is within 100 of', target1)
    else:
        print(i, 'is within 100 of', target2)


# In[ ]:




