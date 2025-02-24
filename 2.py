#Write a program which can compute the factorial of a given numbers. The results should be printed in a comma-separated sequence on a single line. Suppose the following input is supplied to the program: 8 Then, the output should be: 40320

def fact(x):
    if x == 0:
        return 1
    return x * fact(x-1)

x=int(input("Enter the number"))
print(fact(x))


"""def fact_iterative(x):
    result=1
    for i in range(1, x+1):
        result *=i

    return result

x=int(input("Enter the number:-"))
print(fact_iterative(x))
"""

"""num=6

factorial=1

for i in range(1, num+1):
    factorial*=i
print(factorial)"""