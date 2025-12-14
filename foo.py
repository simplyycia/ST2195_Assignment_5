#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 14 20:47:33 2025

@author: staciatan
"""

def is_divisible_by_k(x, k):
  '''
  Checks whether x is divisible by k.
  '''
  return x%k == 0
#indentation- type error 
# change assert to return x%k == 0, assert checks an assumption 
# & crashes if false, doesnt return anything if true
'''
Store all the integers that are multiples of 2 or 5 or 7 that are lower or equal to 1000 (excluding
doubles)
'''
x = [] ## () tuple, cannot edit. change to list x = []
for i in range(1, 1001): # <= 1000
   if is_divisible_by_k(i, 2) or is_divisible_by_k(i, 5) or is_divisible_by_k(i, 7):
    x.append(i)
#change 'and' , '|' to 'or' because we want all integers ≤ 1000 that are divisible by 
#2 or 3 or 7, without double-counting.
'''
Sum all the integers that are multiples of 2 or 5 or 7 that are lower or equal to 1000 (excluding
doubles)
'''
sum(x)
print(sum(x))