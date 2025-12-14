Overview

This assignment focuses on debugging Python code, understanding logical errors, and applying correct control flow and data structures to solve numerical problems accurately.

The goal was not only to produce correct output, but to identify and fix common programming mistakes, including:
	•	incorrect data types
	•	misuse of logical operators
	•	faulty loop conditions
	•	improper function design
	
We were required to:
	1.	Debug an existing function that checks divisibility.
	2.	Correct logic and data type errors in loops.
	3.	Store all integers ≤ 1000 that are divisible by 2 or 3 or 7, without double-counting.
	4.	Compute the sum of these integers.
	
GIVEN code 
def is_divisible_by_k(x, k):
'''
Checks whether x is divisible by k.
'''
assert x%k == 0 
#indentation- type error 
# change assert to return x%k == 0, assert checks an assumption 
# & crashes if false, doesnt return anything if true
'''
Store all the integers that are multiples of 2 or 5 or 7 that are lower or equal to 1000 (excluding
doubles)
'''
x = () #tuple, cannot edit. change to list x = []
for i in range(1000):
if (is_divisible_by_k(x, 2) & is_divisible_by_k(x, 3)) | is_divisible_by_k(x, 7):
x.append(i)
#change 'and' , '|' to 'or' because we want all integers ≤ 1000 that are divisible by 
#2 or 3 or 7, without double-counting.
'''
Sum all the integers that are multiples of 2 or 5 or 7 that are lower or equal to 1000 (excluding
doubles)
'''
sum(x)
#add in print(sum(x))