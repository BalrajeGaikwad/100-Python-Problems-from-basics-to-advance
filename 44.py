"""
Write a program which accepts a string as input to print "Yes" if the string is "yes" or "YES" or "Yes", otherwise print "No".

Hints:

Use if statement to judge condition.
"""

def st(n):
    if n=="yes" or n=="YES" or n=="Yes":
        print("yes")
    else:
        print("no")
n=input()
st(n)