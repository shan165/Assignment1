#!/usr/bin/env python
# coding: utf-8

# In[20]:


# Problem: Use list comprehension to filter number between given bounds [4 Points]
def filter_integers_in_bound(upper_bound, lower_bound, numbers):
    

assert filter_integers_in_bound(3, 9, [12, 3, 6, 9, 4, 0, 24]) == [3, 6, 9, 4]
assert filter_integers_in_bound(-7, 6, [-10, 3, 56, 19, 4, 0, -5]) == [3, 4, 0, -5]


# In[25]:


# Problem: Use set to do following on two set of strings  [4 Points]
def return_number_of_common_words(string1, string2):
    s1=set(string1)
    s2=set(string2)
    return print(s1&s2)
return_number_of_common_words("hi hello", "hi")
return_number_of_common_words("this is testing work", "this is training work") 
return_number_of_common_words("work is in progress", "No one cares") 


# In[1]:



# Problem: apply function on input and return result [2 Points]
def method_runner(function, input_data):
    
    def min(list1):
        n=list1.sort()
        for i in range(1):
            print(i)
            
            
    def f(n1,i):
        sum=0
        for i in n1:
            sum=sum+f(i)
            
        return sum
    method_runner(lambda x: x*x, i)
assert method_runner(foo, 6) == 42


# In[2]:


#Problem: Returns the dictionary of words and their frequency in input string [7 Points]
def get_word_count(input_string):
   result = dict()
   # TODO:implement word count
   str1 = input_string.split()
   for i in str1:
       result[i] = input_string.count(i)
   return result


# In[ ]:




