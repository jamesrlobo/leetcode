# 3913. Sort Vowels by Frequency
# https://leetcode.com/problems/sort-vowels-by-frequency/description/?envType=problem-list-v2&envId=string
# Beats:98.38%
def sortVowels(s):
    d = {}
    for i in s:
        if i in "aeiou" and i not in d:
            d[i] = s.count(i)
    print(d)
    sorted_d = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
    print(sorted_d)
    order = ""
    for i in sorted_d:
        order += d[i]*i
    s = list(s)
    i = 0
    for ch in range(len(s)):
        if s[ch] in "aeiou":
            s[ch] = order[i]
            i+=1
    return "".join(s)

s = "leetcode"
s = "aeiaaioooa"
# s = "baeiou"
print(sortVowels(s))
