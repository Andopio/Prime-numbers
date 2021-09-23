# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 18:48:40 2021

@author: andop
"""
import numpy as np


print('prime numbers')

for n in range(3, 2001, 2):
    top = int(np.sqrt(n))
    prime = True
    for test in range(3, top):
        if n %test == 0:
            prime = False
            break
    if prime: print(n)    