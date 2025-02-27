"""
With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155], write a program to make a list whose elements are intersection of the above given lists.

Hints: Use set() and "&=" to do set intersection operation."""

"""l1=set([1,3,6,78,35,55])
l2=set([12,24,35,24,88,120,155])

l1 &= l2

liii=list(l1)
print(liii)
"""

set1=set([1,3,6,78,35,55])
set2=set([12,24,35,24,88,120,155])
set1 &= set2
li=list(set1)
print(li)