################################################################################
"""
Recommended readings: 
  Chapter on lists: https://automatetheboringstuff.com/3e/chapter6.html 
  List comprehension: https://www.pythonforbeginners.com/basics/list-comprehensions-in-python
"""
################################################################################

"""
Exercise 3.1

Task:
------
Write code that prints the sum of the elements in the following list.
[1, 4, -6, 7, 2, 3, 9, 11, 6]
"""

lst = [1, 4, -6, 7, 2, 3, 9, 11, 6] # In all exercises in this script, you will work with this list
print(sum(lst))
print("Exercise 3.1")

pass

print("---")

"""
Exercise 3.2

Task:
------
Print the product of the elements in the list.
"""
product = 1
for x in lst:
    product *= x
print(product)

print("Exercise 3.2")

pass

print("---")

"""
Exercise 3.3

Task:
------
Print the sum of the squares of the list.
"""
square = 1
sum = 0
for x in lst:
    square=x*x
    sum+=square
print(sum)
print("Exercise 3.3")

pass

print("---")

"""
Exercise 3.4

Task:
------
Print the largest element of the list.
"""
max1 = 0
for x in lst:
    if x>max1:
        max1 = x
print(max1)
print("Exercise 3.4")

pass

print("---")

"""
Exercise 3.5

Task:
------
Print the largest element of the list.
"""
max1 = 0
for x in lst:
    if x>max1:
        max1 = x
print(max1)
print("Exercise 3.5")

pass

print("---")