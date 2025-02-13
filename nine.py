"""
Question£º Write a program that accepts sequence of lines as input and prints 
the lines after making all characters in the sentence capitalized. Suppose the 
following input is supplied to the program: Hello world Practice makes perfect 
Then, the output should be: HELLO WORLD PRACTICE MAKES PERFECT

Hints: In case of input data being supplied to the question, it should be assumed 
to be a console input.
"""

"""lines=[]

while True:
    s=input()
    if s:
        lines.append(s.upper())
    else:
        break;

print(lines)
for sentence in lines:
    print(sentence)
"""

s=input()

result=""
for char in s:
    result+=chr(ord(char)-32) if 'a' <= char <= 'z' else char

print(result)