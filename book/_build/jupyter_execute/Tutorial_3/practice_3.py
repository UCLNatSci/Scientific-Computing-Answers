#!/usr/bin/env python
# coding: utf-8

# # Practice 3
# 
# ## Question 1

# In[1]:


import matplotlib.pyplot as plt

pop = 100
r = 1.1
n = 10

pop_list = [pop]

for i in range(100):
    if i % 5 == 0:
        pop = pop - 31.7
    else:
        pop = pop * r
        pop_list.append(pop)

print(pop_list)

plt.plot(pop_list)


# ## Question 2

# In[2]:


# 1

x1 = []

for i in range(5, 17, 2):
    x1.append(i)

print(x1)

# 2

x2 = []

for i in range(6):
    x2.append(10**i)

print(x2)

# 3

x3 = []

for i in range(9):
    x3.append(i % 3)
    
print(x3)


# ## Question 3

# In[3]:


temp_max = [11, 11, 15, 14, 13, 9, 9, 9, 8, 7]
temp_min = [8, 6, 11, 8, 7, 4, 4, 4, 3, 3]

plt.plot(temp_max, label="Max")
plt.plot(temp_min, label = "Min")
plt.xlabel("Day")
plt.ylabel("Temperature (degrees C)")
plt.legend()
plt.title("Daily Temperature in London")



# ## Question 4
# 
# NB There are many ways to answer this question. The following only uses techniques described in the notes.

# In[4]:



x = [18, 19, 10, 19, 11, 7, 12, 6, 5, 4]
n = len(x)
x1 = []
for i in range(0, n, 2):
    x1.append(x[i])
    
print(x1)

x2 = []
for z in x:
    if z % 2 == 0:
        x2.append(z)
print(x2)
        
x3 = []
for i in range(n):
    x3.append(x[n-i-1])
print(x3)

x4 = [x[0], x[n-1]]
print(x4)

