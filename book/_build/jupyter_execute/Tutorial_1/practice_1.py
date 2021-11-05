#!/usr/bin/env python
# coding: utf-8

# # Practice 1

# ## Question 1
# 
# Recall the definition of factorial of a number $n$:
# 
# $$n! = n \times (n-1) \times \ldots \times 2 \times 1$$
# 
# Use the following pseudocode to calculate the factorial of 10.
# 
# ```none
# Set n to 10
# Set f to 1
# Repeat until n is 1:
#  - Set f to f times n
#  - Decrease n by 1
# Print f
# ```

# In[1]:


n = 10
f = 1
while n > 1:
    f = f * n
    n = n - 1 # or n -= 1
print(f)


# ## Question 2
# 
# Find the 'pseudocode' box in the notes. Write Python code which implements the program described there.
# 
# > The value of a loan increases by 1.3% every month, except in December when it is reduced by 100 pounds. How many months will it take for a 1000 pound loan to reach 2000 pounds?
# 
# How many months does it take if the monthly interest rate is changed to 0.8%?

# In[2]:


# NB the question doesnt specify the starting month, so I have assumed that we start in December. 
# Choosing a different starting month might result in a different answer.

loan = 1000
i = 0
while loan < 2000:
    if i % 12 == 0:
        loan = loan - 100
    else:
        loan = loan * 1.013
    i += 1
print("Number of months:", i)


# ## Question 3
# 
# Write a program which use the quadratic formula to print the solution to the quadratic equation $ax^2 + bx + c = 0$, given variables `a`, `b`, and `c`. Your program should print:
# 
# ```
# The solutions are x = 4 and x = 1
# ```
# or
# ```
# The solution is x = 1
# ```
# or
# ```
# There are no real solutions
# ```
# (Hint: first calculate the discriminant $b^2-4ac$).
# 

# In[3]:


# NB You should test your answer with a variety of values for
# a, b and c to check that it is working correctly.
# At least one test for each of the three type of solution.

a = 1
b = -1
c = -12

discriminant = b**2 - 4 * a * c

if discriminant > 0:
    print("The solutions are x =", (-b + discriminant**0.5)/(2*a), "and x =", (-b - discriminant**0.5)/(2*a))
elif discriminant == 0:
    print("The solution is x =", -b/(2*a))
else:
    print("There are no real solutions")


# ## Question 4
# 
# Given two integers $n$ and $m$ it is possible to perform division-with-remainder by repeatedly subtracting $m$ from $n$ until the result is less than $m$. For example, to calculate 13 divided by 3:
# 
# 13 - 3 = 10  
# 10 - 3 = 7  
# 7 - 3 = 4  
# 4 - 3 = 1  
# 
# 13 divided by 3 equals 4 remainder 1.
# 
# Use the following pseudocode to write a program which performs this calulation.
# 
# > Set `n` to 13  
# > Set `m` to 3  
# > Set `i` to 0  
# > Repeat while `n` is greater than `m`:
# > - Subtract `m` from `n`
# > - Increase `i` by 1.
# >
# > Print the result
# 
# The result should be displayed in words as above (hint: you'll need to create an extra variable to store the original value of `n`).
# 

# In[4]:


n = 13
n_original = n
m = 3
i = 0
while n > m:
    n = n - m
    i += 1
print(n_original, "divided by", m, "equals", i, "remainder", n)

