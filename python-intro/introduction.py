
# coding: utf-8

# # Welcome to the wonderful world of Python!

# ## Basics

# Lets start of by outputing a string

# In[1]:

print('Hello World!')


# Now lets define a variable as an integer

# In[2]:

my_first_int = 10
type(my_first_int)


# And now a float

# In[3]:

my_first_float = 10.0
print(my_first_float)


# And last a string

# In[4]:

my_first_string = 'pythonisthebestthingsinceslicedbread'
print(my_first_string)


# Some mathematical operators:

# In[5]:

a = 10.0
b = 20.0

c = a + b
print("The value of c is " + str(c))

d = c - a
print("The value of d is " + str(d))

e = a / b
print("The value of e is " + str(e))

f = a**b
print("The value of f is " + str(f))


# ## Arrays

# In[6]:

x = [1,3,5,7,9]
print(x)


# In[7]:

print(x[0])


# In[8]:

print(x[:])


# In[9]:

print(x[2:])


# In[10]:

print(x[:3])


# ## Loops

# A simple for loop

# In[11]:

for x in range(0,10):
    print(x)


# And a while loop

# In[12]:

count = 0
while (count < 10):
    print(count)
    count = count + 1


# ## Conditionals

# In[13]:

numbers = [1,2,3,4,5,6]

for x in numbers:
    if(x % 2 == 0):
        print(str(x) + " is even")
    else:
        print(str(x) + " is odd")


# ## References

# As all objects in python are by reference, we quickly have a look at how this affects us:

# In[14]:

x = [1,2,3,4,5]
y = x
x.append(7)
print(y)


# In[15]:

x = [1,2,3,4,5]
y = x[:] # slice the list, makes a copy of the array
x.append(7)
print(y)


# ## Functions

# In[16]:

def add(a,b):
    c = a + b
    return c

print("The results of 1 + 2 = " + str(add(1,2)))


# ## NumPy

# Modules are imported using the "import" statement in python

# In[17]:

import numpy as np


# Numpy is now imported in the local namespace as np, lets check the version number

# In[18]:

print(np.__version__)


# NumPy has many functions of which most we will not use. We will try to give you a introduction to some of the most commonly used ones

# In[19]:

x = np.zeros([10,10])


# In[20]:

print(x)


# In[21]:

print(x.shape)


# Define a equally spaced array

# In[22]:

help(np.linspace)


# In[23]:

x = np.linspace(2.0, 3.0, num=5)
print(x)


# Multiply with a scalar

# In[24]:

y = x * 5
print(y)


# Define a matrix

# In[25]:

a = np.matrix([[1, 2], [3, 4]])
print(a)


# Matrix multiplication

# In[26]:

b = a*a
print(b)


# Elementwise multiplication

# In[27]:

b = np.multiply(a,a)
print(b)


# Sum along axis 0,1 and all

# In[28]:

print(np.sum(a, axis=0))


# In[29]:

print(np.sum(a, axis=1))


# In[30]:

print(np.sum(a))


# Now, lets transpose a matrix

# In[31]:

a = np.ones([10,4,2])
print(a.shape)


# In[32]:

print(a.transpose().shape) #no axes argument reverses the order of the axis


# In[33]:

print(a.transpose(1,0,2).shape)

