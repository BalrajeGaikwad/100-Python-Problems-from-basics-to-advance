"""
Question: Write a program which accepts a sequence of comma separated 4 digit binary numbers
as its input and then check whether they are divisible by 5 or not. The numbers that are divisible 
by 5 are to be printed in a comma separated sequence. Example: 0100,0011,1010,1001 Then the output 
should be: 1010 Notes: Assume the data is input by console.

"""
"""value = []
items=[x for x in input().split(',')]
print(items)
for p in items:
    intp = int(p, 2)
    if not intp%5:
        value.append(p)

print(','.join(value))"""


values=[]
items=[x for x in input().split(',')]
for p in items:
    intp=int(p,2)
    if not intp%5:
        values.append(p)
print(','.join(values))