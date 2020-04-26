#!/usr/bin/env python
# coding: utf-8

# In[7]:


# Problem: Write a code that takes number from user and print if number is even or odd 
n=int(input("entre num:"))
if n % 2 == 0 :
    print("even")
else : 
     print("odd")


# In[24]:


# Problem: Merge two list 
def merge_list(first_list,second_list):
    return first_list+second_list
first_list=['a', '34', 89, 2.3]
second_list=['b','67']  

merge_list(first_list,second_list)


# In[20]:


# Write a code to print numbers divisible by given number in given range  
def give_divisible(start_number, end_number, divider):
    # TODO: write code
    result = []
    for i in range(star_number,end_number):
        if i % divider == 0:
            result.append(i)
    return result
assert give_divisible(1, 10, 2) == [2, 4, 6, 8]
assert give_divisible(3, 16, 3) == [3, 6, 9, 12, 15]
assert give_divisible(1, 5, 7) == []

        


# In[21]:


#Write a code that counts even and odd numbers in list
def count_even_odd(numbers):
    even_count = 0
    odd_count = 0
    for i in numbers :
        if i % 2 == 0:
            even_count=even_count+1
        else:
            odd_count=odd_count+1
    return even_count, odd_count
assert count_even_odd([2, 3, 5, 6, 7]) == (2, 3)
assert count_even_odd([17, 23, 65]) == (0, 3)
assert count_even_odd([12, 4, 80]) == (3, 0)
    


# In[ ]:




