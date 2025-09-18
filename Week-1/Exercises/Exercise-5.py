# Helper function: Ignore
def sprint(s):
    if __name__ == "__main__":
        print(s)

################################################################################
"""
Recommended readings: 
  Chapter on functions: https://automatetheboringstuff.com/3e/chapter4.html
"""
################################################################################

"""
Exercise 5.1

Task:
------
Go back to the code you wrote for exercise 2.7 and turn it into a function called print_triangle_o.
The function should take one argument called 'rows' and print a triangle out of 'o's with n rows.
"""
sprint("Exercise 5.1")
def print_triangle_o(rows):
    for i in range(1, rows + 1):
        spaces = " " * (rows - i)
        os = "o" * (2 * i - 1)
        line = spaces + os + spaces
        print(line)



print_triangle_o(7)


sprint("---")

"""
Exercise 5.2

Task:
------
Go back to the code you wrote for exercise 3.2 and turn it into a function called prod_list_easy.
You can assume that all the elements of the list are numbers.
"""

sprint("Exercise 5.2")

def prod_list_easy(lst):
    product = 1
    for x in lst:
        product *= x
    return product
numbers = [2, 3, 4]
print("Product of", numbers, "=", prod_list_easy(numbers))
sprint("---")

"""
Exercise 5.3

Task:
------
Go back to the code you wrote for exercise 3.2 and turn it into a function called prod_list_rec.
You can assume that all the elements of the list are numbers but you are not allowed to use
loops.

Hint: Can you think of a recursive way to do it?
------
"""
sprint("Exercise 5.3")
def prod_list_rec(lst):
    if not lst:
        return 1
    return lst[0] * prod_list_rec(lst[1:])

numbers = [2, 3, 4]
print("Product of", numbers, "=", prod_list_rec(numbers))




sprint("---")

"""
Exercise 5.4

Task:
------
Take the function body you wrote in the previous exercise and modify it so that it stops
executing in case not all of the elements of the list are numbers.

Hint: The product of the empty set is 1.
------
"""

sprint("Exercise 5.4")

def prod_list_rec_full(lst):
    if not lst:
        return 1


    if not isinstance(lst[0], (int, float)):
        print("Error: list contains non-numeric element:", lst[0])
        return None


    rest_product = prod_list_rec_full(lst[1:])
    if rest_product is None:
        return None
    return lst[0] * rest_product
print("Product of [2, 3, 4]:", prod_list_rec_full([2, 3, 4]))
print("Product of [2, 'a', 4]:", prod_list_rec_full([2, 'a', 4]))
    
sprint("---")

"""
Exercise 5.5

Task:
------
Once you have solved Exercises 5.1 to 5.4, uncomment the following lines of code
and run the script again. The lines of code test the functions you wrote against
expected outputs. If you solved the exercises correctly, the script will tell you.
------
"""

#Run test cases
if __name__ == "__main__":
     from testcases import (
         run_tests_ex51,
         run_tests_ex52,
         run_tests_ex53,
         run_tests_ex54,
     )

     run_tests_ex51()
     run_tests_ex52()
     run_tests_ex53()
     run_tests_ex54()