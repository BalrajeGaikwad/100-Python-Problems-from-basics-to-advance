"""
Please write a program to generate all sentences where subject is in ["I", "You"] and verb is in ["Play", "Love"] and the object is in ["Hockey","Football"].

Hints: Use list[index] notation to get a element from a list.
"""

subject=["I","You"]
verbs=["Play","Love"]
objects=["Hockey","Football"]
for i in range(len(subject)):
    for j in range(len(verbs)):
        for k in range(len(objects)):
            sentence="%s %s %s." % (subject[i], verbs[i], objects[k])
            print(sentence)