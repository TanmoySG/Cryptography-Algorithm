#!/usr/bin/env python
# coding: utf-8

# # Primitive Roots

# ## About 
# In modular arithmetic, a branch of number theory, a number g is a primitive root modulo n if every number a coprime to n is congruent to a power of g modulo n. That is, g is a primitive root modulo n if for every integer a coprime to n, there is an integer k such that g<sup>k</sup> ≡ a (mod n).

# ## Algorithm
# 
# **x** is the **primitive root of q** if,
# 
# **{x<sup>1</sup> mod q, x<sup>2</sup> mod q, x<sup>3</sup> mod q, ..., x<sup>q-1</sup> mod q} => {1, 2, 3, ..., q-1}**
# 
# 1. Calculate value of **x<sup>i</sup> mod q**, for **x <= q-1 and i <= q-1**
# 2. The value of x, for which the corresponding set(s), **{x<sup>1</sup> mod q, x<sup>2</sup> mod q, x<sup>3</sup> mod q, ..., x<sup>q-1</sup> mod q} => {1, 2, 3, ..., q-1}** , is a a **Primitive Root of q**
# 3. Print the Primitive Root table.
# 4. Print the list of Primitive roots.

# In[122]:


import random
from termcolor import colored

def primitiveRoot(q):
    setOfPR = []
    a = 1
    print("\nPrimitive Roots table for {} : \n".format(q))
    print(colored("a\u2193     i\u2192|".format(q) , 'blue'), end="    ")
    for i in range(1, q):
        print(colored('a^{} mod {}'.format(i,q), 'blue'), end="    ")
    print("\n")
    for i in range(1, q+1):
        print(colored('------------', 'blue'), end="")
    print("\n")
    while a<q:
        rootSet= []
        reqSet = []
        for i in range(1, q):
            rootSet.append(int((a**i)%q))
        #print(rootSet)
        print(colored("{}        |".format(a) , 'blue'), end="        ")
        for j in range(1, q):
            reqSet.append(j)
        
        if set(rootSet) == set(reqSet):
            setOfPR.append(a)
            for k in rootSet:
                print(colored("{}".format(k), 'green'), end="            ")
            print("\n")
            a += 1
        else:
            for k in rootSet:
                print("{}".format(k), end="            ")
            print("\n")
            a += 1
    print("\nPrimitive Roots of {} are ".format(q), setOfPR, end="\n\n")

q = int(input("Enter a prime number: "))

primitiveRoot(q)


# #### Tanmoy Sen Gupta
# [tanmoysg.com](http://tanmoysg.com) | +91 9864809029 | tanmoysps@gmail.com
