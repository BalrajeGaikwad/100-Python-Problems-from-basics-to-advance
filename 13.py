"""
Question: Write a program that accepts a sentence and calculate the number of letters and digits. 
Suppose the following input is supplied to the program: hello world! 123 Then, the output should 
be: LETTERS 10 DIGITS 3
"""
s=input()
dict={ 'LETTERS':0 , 'DIGITS':0}
for c in s:
    if c.isdigit():
        dict['DIGITS']+=1
    elif c.isalpha():
        dict['LETTERS']+=1
    else:
        pass
print("LETTERS", dict['LETTERS'])
print("DIGITS",dict['DIGITS'])