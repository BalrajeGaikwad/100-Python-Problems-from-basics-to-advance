"""
Define a function that can accept an integer number as input and print the "It is an even number" if the number is even, otherwise print "It is an odd number".
"""

def check(n):
    if n%2==0:
        print("It is an even number")
    else:
        print("odd number")

check(7)