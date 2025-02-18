"""
Write a program which can filter even numbers in a list by using filter function. The list is: [1,2,3,4,5,6,7,8,9,10].

Hints:

Use filter() to filter some elements in a list. Use lambda to define anonymous functions.
"""

"""li=[1,2,3,4,5,6,7,8,9,10]
evennumber=filter(lambda x: x%2==0, li)
print(evennumber)"""

# Given list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Using filter() with a lambda function to get even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

# Print the filtered even numbers
print(even_numbers)
