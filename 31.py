"""
Define a function that can accept two strings as input and print the string with maximum length in console. If two strings have the same length, then the function should print al l strings line by line.

Hints:

Use len() function to get the length of a string
"""

def value(s1,s2):
    len1=len(s1)
    len2=len(s2)

    if len1>len2:
        print(s1)

    elif len2>len1:
        print(s2)
    else:
        print(s1)
        print(s2)
value("one","three")