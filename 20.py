"""
Question: Define a class with a generator which can iterate the numbers, which are divisible by 7, 
between a given range 0 and n.
"""

def putNumbers(n):
    i = 0
    while i < n:
        j = i
        i = i + 1
        if j % 7 == 0:
            yield j  # This makes the function a generator

# Use reversed() on the generated numbers
for i in reversed(list(putNumbers(100))):
    print(i)
