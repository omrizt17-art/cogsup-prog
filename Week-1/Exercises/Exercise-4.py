################################################################################
"""
Recommended readings: 
  Chapter on dictionaries: https://automatetheboringstuff.com/3e/chapter7.html 
  Iterating through dictionaries: https://realpython.com/iterate-through-dictionary-python/
"""
################################################################################

"""
Exercise 4.1

Task:
------
Print the sum of the values in the dictionary.
"""

dct = {'a': 3, 'b': 7, 'c': -2, 'd': 10, 'e': 5}
print("Sum of values:", sum(dct.values()))
print("Exercise 4.1")

pass

print("---")

"""
Exercise 4.2

Task:
------
Print the key that has the largest value in dct.
"""
max_key = max(dct, key=dct.get)
print("Key with largest value:", max_key)
print("Exercise 4.2")

pass

print("---")

"""
Exercise 4.3

Task:
------
Create a new dictionary with the squares of all the values in dct.
"""
squared_dct = {k: v**2 for k, v in dct.items()}
print("Dictionary with squared values:", squared_dct)
print("Exercise 4.3")

pass

print("---")

"""
Exercise 4.4

Task:
------
Print only the keys in dct whose values are even numbers.
"""
even_keys = [k for k, v in dct.items() if v % 2 == 0]
print("Keys with even values:", even_keys)
print("Exercise 4.4")

pass

print("---")

"""
Exercise 4.5

Task:
------
Create a new dictionary that swaps the keys and values in dct.
"""
swapped_dct = {v: k for k, v in dct.items()}
print("Swapped dictionary:", swapped_dct)
print("Exercise 4.5")

pass

print("---")

"""
Exercise 4.6

Task:
------
Count the number of times each letter appears in the string 'ccctcctttttcc'
and print the resulting dictionary.
"""

s = 'ccctcctttttcc'
count_dct = {}
for ch in s:
    count_dct[ch] = count_dct.get(ch, 0) + 1
print(count_dct)
print("Exercise 4.6")

pass

print("---")

"""
Exercise 4.7

Task:
------
Given the dictionary of responses_mapping = {'j':'jazz', 'p':'pop'},
and the string responses = 'jjjpjjpppppjj',
print the list of corresponding words.
"""

responses_mapping = {'j':'jazz','p':'pop'}
responses = 'jjjpjjpppppjj'
words = [responses_mapping[ch] for ch in responses]
print("Mapped words:", words)
print("Exercise 4.7")

pass

print("---")

"""
Exercise 4.8

Task:
------
Merge the following two dictionaries into one:
{'a': 1, 'b': 2} and {'c': 3, 'd': 4}
"""
d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
merged = d1.copy()
merged.update(d2)
print("Merged dictionary:", merged)
print("Exercise 4.8")

pass

print("---")

"""
Exercise 4.9

Task:
------
Starting from the dictionary {'zebra': 10, 'dolphin': 25, 'alligator': 3, 'monkey': 5, 'pig': 9},
create a new one whose keys are sorted alphabetically.
"""
animals = {'zebra': 10, 'dolphin': 25, 'alligator': 3, 'monkey': 5, 'pig': 9}
sorted_animals = {}
for k in sorted(animals):
    sorted_animals[k] = animals[k]
print(sorted_animals)
print("Exercise 4.9")

pass

print("---")

"""
Exercise 4.10

Task:
------
Starting from the dictionary {'zebra': 10, 'dolphin': 25, 'alligator': 3, 'monkey': 5, 'pig': 9},
create a new one whose values appear in increasing order.
"""
animals = {'zebra': 10, 'dolphin': 25, 'alligator': 3, 'monkey': 5, 'pig': 9}

sorted_by_values = {}

for k, v in sorted(animals.items(), key=lambda item: item[1]):
    sorted_by_values[k] = v   

print(sorted_by_values)

print("Exercise 4.10")

pass

print("---")