"""
Question: Write a program that accepts a sentence and calculate the 
number of upper case letters and lower case letters. Suppose the 
following input is supplied to the program: Hello world! Then, 
the output should be: UPPER CASE 1 LOWER CASE 9
"""

s=input()
d={ "UPPER CASE": 0, "LOWER CASE":0}
for c in s:
    if c.islower():
        d["LOWER CASE"]+=1
    elif c.isupper():
        d["UPPER CASE"]+=1
    else:
        pass
print("lower",d["LOWER CASE"])
print("upper",d["UPPER CASE"])