#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Max Mattern
# M03 Tutorial Functional vs OOP Programming-57
# SDEV220 Fall 2022
# 11/14/22

# 1: Write a function that computes the volume of a sphere given its radius.

def vol(rad):
    return (4/3)*3.14*(rad**3)
vol(2)


# In[7]:


# 2: Write a function that checks whether a number is in a given range (inclusive of high and low).

def ran_check(num,low,high):
    if num in range(low,high+1):
        print(f'{num} is in range of {low} and {high}')
    else:
        print('not in range')

ran_check(5,2,7)


# In[9]:


# 3: Write a function that accepts a string and calculates the number of upper case and lower case letters.

def up_low(s):
    d = {'upper':0,'lower':0}
    
    for char in s:
         if char.isupper():
             d['upper'] += 1
         elif char.islower():
             d['lower'] += 1
         else:
             pass
    
    print(f"Origional String: {s}")
    print(f'Lowercase count: {d["lower"]}')
    print(f'Uppercase count: {d["upper"]}')
         
s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
up_low(s)


# In[13]:


# 4: Write a function that takes a list and returns a new list with unique elements of the first list.

def unique_list(lst):
    return list(set(lst))

unique_list([1,1,1,1,2,2,3,3,3,3,4,5])


# In[15]:


# 5: Write a function to multiply all the numbers in a list.

def multiply(numbers):
    total = 1
    for num in numbers:
        total = total*num
    return total

multiply([1,2,3,-4])


# In[17]:


# 6: Write a function that checks whether a word or phrase is palindrome or not.

def palindrome(s):
    # emove spaces from string
    s = s.replace(' ','')
    # Check if string is == revered version of the string
    return s == s[::-1]

palindrome('nurses run')


# In[20]:


# 7: Write a function to check whether a string is panagram or not. (Assume the string
#    passed in does not have any punctuation)

import string

def ispangram(str1, alphabet=string.ascii_lowercase):
    
    # Create a set of the alphabet
    alphaset = set(alphabet)
        
    # Remove any spaces from the input string
    str1 = str1.replace(' ','')
    
    # Convert into all lowercase
    str1 = str1.lower()
    
    # Grab all unique letters from the string set()
    str1 = set(str1)
    
    # alphabet set == string set input
    return str1 == alphaset

ispangram("The quick brown fox jumps over the lazy dog")
    


# In[ ]:





# In[ ]:




