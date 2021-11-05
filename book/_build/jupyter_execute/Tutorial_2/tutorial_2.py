#!/usr/bin/env python
# coding: utf-8

# # Tutorial 2
# 
# ## Question 1
# 
# Use `for` loops and `print(end="")` to write functions which print the following patterns:
# 
# 1. `print_square(n)` where `n` is the number of stars along each edge.
# 
# ```
# *****
# *   *
# *   *
# *   *
# *****
# ```
# 2. `print_rhombus(n)` where `n` is the number of stars along each edge.
# 
# ```
#     *****
#    *   *
#   *   *
#  *   *
# *****
# ```
#  
# 3. `print_numbers(n)` where `n` is the number at the centre.
# 
# ```
# 1       1
#  2     2
#   3   3
#    4 4
#     5
#    4 4
#   3   3
#  2     2
# 1       1
# ```

# In[1]:


# this question is perhaps harder than it intially looks.
# The key is to take it break it down into individual steps before
# starting  to write any code.

def print_square(n):
    for i in range(n):
        print("*", end="")
    print()
    for i in range(n - 2):
        print("*", end = "")
        for j in range(n - 2):
            print(" ", end="")
        print("*")
    for i in range(n):
        print("*", end="")
    print()
        
def print_rhombus(n):
    for i in range(n-1):
        print(" ", end="")
    for i in range(n):
        print("*", end="")
    print()
    for i in range(n - 2):
        for j in range(n - 2 - i):
            print(" ", end="")
        print("*", end="")
        for j in range(n-2):
            print(" ", end="")
        print("*")
    for i in range(n):
        print("*", end="")
    print()
print_square(5)
print()
print_rhombus(5)


# ## Question 2
# 
# An integer $n$ is a *prime number* if it is divisible only by 1 and $n$. 
# 
# 1. Write a function `is_divisible(n, m)` which returns `True` if `n` is divisible by `m`, and otherwise returns `False`.
# 1. Write a function `is_prime(n)` which returns `False` if `n` is divisible by any integer between `2` and `n-1`, and otherwise returns `True`.
# 1. Write a function `number_of_primes(n)` which returns the number of prime numbers less than or equal to `n` [NB 1 is *not* a prime number].
# 
# Check the correctness of your functions by writing two tests for each.

# In[2]:


# It is crucial to understand how the importance of the return statement.
# The return statement determines the *output* of the function.
# For 1 and 2 the function shoud return a value of True or False.

# 1. The expression n % m == 0 is True if n is divisible m; otherwise false
def is_divisible(n, m):
    return n % m == 0

# 2. Construct a loop and *immediately* exit the function as soon as
# a value which divides into n. Only if no such value is found will the final return statement be reached.
def is_prime(n):
    for m in range(2, n):
        if is_divisible(n, m):
            return False
    return True

def number_of_primes(n):
    i = 0
    for m in range(2, n+1):
        if is_prime(m):
            i += 1
    return i
            
print("4 is divisible by 2:", is_divisible(4, 2))
print("4 is divisible by 3:", is_divisible(4, 3))

print("7 is a prime number:", is_prime(7))
print("8 is a prime number:", is_prime(8))

print("Number of prime numbers up to 10:", number_of_primes(10))
print("Number of prime numbers up to 11:", number_of_primes(11))
    
    


# ## Question 3
# 
# A [solid of revolution](https://en.wikipedia.org/wiki/Solid_of_revolution) is a three-dimensional figure contstructed by rotating a curve about a straight line. We can estimate the volume of a solid of revolution by dividing it into a sequence of stacked discs and summing the volume of each.
# 
# A sphere of radius $R$ is formed by rotating the curve $y = \sqrt{R^2 - x^2}$ around the x-axis between $-R$ and $R$.
# 
# ![a](https://miro.medium.com/max/2400/0*d7QEcno6XhPOiJSt.png)
# 
# Use the following steps to estimate the volume of a sphere of radius 1.
# 
# 1. Write a function `vol_disc(R, x, dx)` which returns the volume of the disc centred at position `x` with thickness `dx`. 
# 1. Estimate the volume of a sphere of radius 1 by dividing the figure into 10 discs equally spaced between `-1` and `1` [use a value of 3.14159 for $\pi$].
# 1. Write a function `sphere_vol(R, n)` which returns the estimate of the volume of a sphere of radius `R` calculated by dividing it into `n` discs.
# 1. The estimate should get more accurate as we increase `n`. We can estimate the accuracy by calculating the difference between `sphere_vol(R, n)` and `sphere_vol(R, n-1)`. For `R = 1`, how large does `n` need to be so that difference between consecutive estimates is less than $10^{-4}$?

# In[3]:


# This question is designed to allow you to combine loops and functions together.
# It is a very typical example of how we might perform a computation in scientific computing.
# If you couldn't complete it this time it would make excellent exam preparation!

# 1. Writing the function first allows to test this code separately from the remaining complexity
# of the problem. 

def vol_disc(R, x, dx):
    r = (R**2 - x**2)**0.5
    return 3.14159 * r ** 2 * dx
    # We hardcode the value of pi here. Later you will learn about numpy, a mathematical
    # library containing many useful functions, including a value for pi.

# 2. We first set variables containing values we will use in the computation.
vol = 0
dx = 2 / 10 # width of each disc
for i in range(10):
    x = -1 + (i / 10) * 2 # the x position of the left-hand edge of each disc
    vol += vol_disc(1, x, dx)
    
print("Volume of sphere radius 1:", vol)

# let's check it against the formula vol = (4/3)*pi*r**3
print("4/3 * pi * 1^3:", (4/3) * 3.14159)

# 3. It would be a good idea to draw a diagram before writing this code. 

def sphere_vol(R, n):
    vol = 0
    dx = 2 * R / n
    pi = 3.14159
    for i in range(n):
        x = -R + (i / n) * 2 * R # x is the position of the  left-hand edge of each disc
        vol += vol_disc(R, x, dx)
    return vol

# 4. Use a while loop so that we terminate once we reach the required level of accuracy
        
diff = 1
vol = 0
n = 2
while diff > 1e-4:
    vol_prev = vol
    vol = sphere_vol(1, n)
    diff = vol - vol_prev
    # could use np.abs here instead (when you learn about numpy)
    if diff < 0:
        diff = diff * -1
    n += 1
    # print("vol:", vol)
    # print("diff:", diff)
        
print(n)
print(vol)
    

