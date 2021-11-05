#!/usr/bin/env python
# coding: utf-8

# # Tutorial 1
# 
# ## Question 1
# A time `t` in seconds can be converted to days, hours, minutes and seconds using integer division:
# 
# 1. Divide `t` by 60; set `t` to the quotient and call the remainder `s`.
# 1. Divide `t` by 60; set `t` to the quotient and call the remainder `m`.
# 1. Divide `t` by 24; set `d` to the quotient and call the remainder `h`.
# 
# Calculate the number of days, hours, minutes and seconds in one million seconds. Display the result as follows:
# ```
# 1000000 seconds is xx days H:M:S
# ```

# In[1]:


# It should be reasonably easy to follow the instructions in order to produce the correct code to perform the calculation.
# The only tricky part is to maintain the original value of `t` in a new variable `t_orig` so that we can include it in the final print statement.

t = 1000000
t_orig = t
s = t % 60
t = t // 60
m = t % 60
t = t // 60
h = t % 24
d = t // 24

print(t_orig, " seconds is ", d, " days ", h, ":", m, ":", s, sep="")


# ## Question 2
# 
# Iodine-131 is a radioisotope with a half-life $t_\mathrm{half} = 8.02$ days.
# 
# 1. Use the equation $r = \left(\frac{1}{2}\right) ^ {1/t_\mathrm{half}}$ to calculate the daily decay rate (i.e. the proportion of a sample of Iodine 131 that decays in one day).
# 1. A sample of radioactive material containing Iodine-131 has an activity of $1.67 \times 10^{12}$ Becquerels. Write a program which calculates the number of days it takes for the sample to reach an activity of $10000$ Becquerels.
# 1. Print the activity of the sample once every 7 days.

# In[2]:


# This is very similar to the bacterial growth example in the notes.
# You shouldn't need to know much about radioactive decay to answer this.
# However, this is the kind of foundational knowledge that I would expect all Natural Scientists to be aware of,
# even if you don't specialise in physics.

t_half = 8.02
r = 0.5 ** (1/t_half)
print("Daily decay rate:", r)

activity = 1.67e12

i = 0
while activity > 10000:
    
    activity = activity * r
    
    i += 1 # or i = i + 1
    
    if i % 7 == 0:
        print(activity)
    
print("Number of days:", i)


# ## Question 3
# 
# We can calculate how many digits there are in a number by repeatedly dividing by 10 until the number is less than one.
# 
# 1. Write peudo-code for this calculation.
# 1. Write a Python program to implement it, displaying the result in the format `1234 has 4 digits.`
# 1. Test your program with a variety of numbers.
# 1. Extend your program so that it works for negative numbers.
# 

# 
# 
# 1. Pseudocode.
# 
# This is just an example. It is most important that it makes sense to you. Notice that each line corresponds to one line of Python.
# ```
# set value of x
# set y to value of x
# set i = 0
# repeat until x less than 1:
#     divide x 10
#     increase i by 1
# display value of y and i
# ```

# In[3]:


# 2.

x = 1234
y = x
i = 0
while x > 1:
    x = x / 10
    i += 1
print(y, "has", i, "digits")

#3.

# Change the value of x in the code above and test that the result is correct.
# It's a good idea to test 'edge cases' such as 1000, 99999

#4.

# The simplest way to do this is to multiply x by -1 if it is negative.
# This is quite a clever 'trick' that allows us to re-use our existing code!

x = -1234.
y = x
if x < 0:
    x = x * -1
    
i = 0
while x > 1:
    x = x / 10
    i += 1
print(y, "has", i, "digits")


# ## Question 4 (The Collatz Problem)
# 
# Given a positive integer `n`, the Collatz Operation is defined as follows:
#     
#  - If the number is even, divide it by two
#  - If the number is odd, triple it and add one
#  
# Repeatedly applying the Collatz Operation results in a sequence of integers which eventually reaches the number 1.
# 
# > Write a program which generates the Collatz Sequence for a given positive integer $n$. 
# 
# For example, if $n = 5$ then your program should produce the following:
# 
# ```
# 5
# 16
# 8
# 4
# 2
# 1
# ```
# 
# Given a positive integer $n$, define the Collatz Number to be the length of the Collatz Sequence for $n$. For example, the Collatz number of 5 is 6.
# 
# > Write a program which calculates and prints the Collatz number of a given number $n$. For example, if $n=5$ your program should print `The Collatz number of 5 is 6`.
# 
# > Write a program which finds the smallest number $n$ whose Collatz Number is greater than 200.
# 

# In[4]:


# Despite a completely different problem, we can use a very similar pattern that 
# we used in the previous two questions. 

n = 5
m = n
i = 1
while n > 1:
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3*n + 1
    i += 1 
print("The Collatz Number of", m, "is", i)


# In[5]:


# The second part is tricky because we need to repeat the previous
# code for sequential numbers. But we already know how to do this:
# using while loops. Thus, we have a while loop within a while loop.
# The outer one terminates when we reach a collatz number greater than 200.

# Keeping track of the various variables is difficult and it might take some
# perseverence to get this right. Using a function to encapsulate the inner loop
# might make it easier - but we haven't studied functions yet.

n = 1
i = 1
while i <= 200: # while i is less than *or equal to* 200
    i = 1
    m = n
    while m > 1:
        if m % 2 == 0:
            m = m // 2
        else:
            m = 3 * m + 1
        i += 1

    print(n, i)
    n = n + 1
    
print("The Collatz Number of ", n - 1, "is", i) #note that we have to subract 1 from 


# In[ ]:




