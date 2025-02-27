"""
With a given list [12,24,35,24,88,120,155,88,120,155], write a program to print this list after removing all duplicate values with original order reserved.

Hints: Use set() to store a number of values without duplicate."""

def re(li):
    new=[]
    seen=set()
    for item in li:
        if item not in seen:
            seen.add(item)
            new.append(item)

    return new
li=[12,24,35,24,88,120,155,88,120,155]
#print(removeDuplicat((li)))
print(re(li))