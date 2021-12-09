#!/usr/bin/env python
# coding: utf-8

# # Practice 6
# ## Question 1

# In[1]:


import matplotlib.pyplot as plt

data = []
with open("monthly-sunspots.txt") as f:
    for line in f:
        data.append(float(line))
        
plt.plot(data)


# ## Question 2

# In[2]:


from time import time
with open("current_time.txt", "a") as f:
    f.write(str(time()) + "\n")


# ## Question 3

# In[3]:


import csv
with open("periodic_table.csv") as f:
    reader = csv.reader(f) # create a reader object from the file
    next(reader) # ignore the header row of the CSV file
    i = 1
    for row in reader: 
        num = int(row[0]) 
        name = row[1]
        description = row[3]
        with open("element_" + str(num) + ".txt", "w") as f:
            f.write(name + "\n")
            f.write(description)
        if i >= 9:
            break
        i += 1

