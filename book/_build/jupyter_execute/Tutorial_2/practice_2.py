#!/usr/bin/env python
# coding: utf-8

# # Practice 2

# ## Questions 1 - 3

# In[1]:


import matplotlib.pyplot as plt
import numpy as np

# function definitions

# 1.

def draw_square():
    draw_forward(1)
    rotate_left(90)
    draw_forward(1)
    rotate_left(90)
    draw_forward(1)
    rotate_left(90)
    draw_forward(1)
    
# 2.

def draw_polygon(n, dis):
    for i in range(n):
        draw_forward(dis)
        rotate_left(360/n)

# 3.

def draw_rotated_polygons(n, m):
    for i in range(m):
        draw_polygon(n, 1)
        rotate_left(360/m)
        
def start():
    state[0] = 0
    state[1] = 0
    state[2] = 0
    
    plt.figure(figsize=(5,5))
    plt.xlim(-2, 2)
    plt.ylim(-2, 2) 

def draw_forward(dis):
    x = state[0]
    y = state[1]
    angle = state[2]
    state[0] = x + dis * np.cos(angle)
    state[1] = y + dis * np.sin(angle)
    plt.plot([x, state[0]], [y, state[1]], color="black", linewidth=2)
    
def rotate_left(theta):
    state[2] = state[2] + theta * np.pi / 180
    
state = [0, 0, 0]

# Turtle instructions

# 1. NB mistake in question - should be draw_forward()
    
start()
draw_forward(2)
rotate_left(90)
draw_forward(2)
rotate_left(90)
draw_forward(2)
rotate_left(90)
draw_forward(2)

# NB I've brought the call to start() outside the function
# so that we can later chain these functions together

start()
draw_square()

# 2. 
start()
draw_polygon(6, 1)
    
# 3.

start()
draw_rotated_polygons(4, 5)


# ## Question 4
# 
# Copy the three function definitions `get_number_of_day`, `get_day_of_week` and `print_day_of_week_from_number_of_year` from the notes. Correct the code so that it prints the day of the week correctly.

# In[2]:


# It turns out there were *two* mistakes in the function! 

def get_number_of_day(n):
    d = (n - 1) % 7 # subract 1 from n
    return d # changed from n to d

def get_day_of_week(n):
    week_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return week_days[n]

def get_day_of_week_from_number_of_year(n):
    d = get_number_of_day(n)
    s = get_day_of_week(d)
    return s

# should print 0
get_number_of_day(1)

# Should print "Monday"
day = get_day_of_week_from_number_of_year(1)
print(day)



# ## Question 5

# In[3]:


#Two nested loops
#Remember range(a, b) runs from a to b-1
for i in range(1, 11):
    for j in range(1, 11):
        print(i*j, end=" ") # use the end argument to print a space rather than a new line
    print() # print a new line after each iteration of the inner loop
    
    
# NB to print it nicely with everything lined up requires a little more work.
# we could do this with 'if' statements to print the correct number of spaces
# or use a more advanced techniques such as string.format (which we haven't covered yet)

