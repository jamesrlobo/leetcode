# 1417. Reformat The String
# Reference: https://www.geeksforgeeks.org/python/iterate-over-two-lists-with-different-lengths-in-python/
from itertools import zip_longest

def reformat(s):
    cntLetters, cntDigits = [], []
    res = ""
    for i in s:
        if i.isdigit():
            cntDigits.append(i)
        else:
            cntLetters.append(i)
    if (len(cntLetters) - len(cntDigits)) in [-1, 0, 1]:
        if len(cntLetters) >= len(cntDigits):
            for i, j in zip_longest(cntLetters, cntDigits):
                if i != None:
                    res += str(i)
                if j != None:
                    res += str(j)
            return res
        else:
            for i, j in zip_longest(cntDigits, cntLetters):
                if i != None:
                    res += str(i)
                if j != None:
                    res += str(j)
            return res
    else:
        return ""

# s = "a0b1c2"
# s = "covid2019"
s = "ab123"
print(reformat(s))
