"""
Question: Write a program that accepts a sequence of whitespace separated words as input and prints the 
words after removing all duplicate words and sorting them alphanumerically. Suppose the following input 
is supplied to the program: hello world and practice makes perfect and hello world again Then, the output 
should be: again and hello makes perfect practice world

Hints: In case of input data being supplied to the question, it should be assumed to be a console input. 
We use set container to remove duplicated data automatically and then use sorted() to sort the data.
"""

s=input()
words=[word for word in s.split(" ")]
print(" ".join(sorted(list(set(words)))))


"""
another way
s=input()
words=s.split(" ")
unique_words=set(words)
sorted=sorted(unique_words)
result=" ".join(sorted)
print(result)"""


"""
s = input()  
words = s.split(" ")
unique_words = set()
for word in words:
    unique_words.add(word)

sorted_words = sorted(unique_words)
# Join the sorted words into a single string and print
result = " ".join(sorted_words)
print(result)
"""