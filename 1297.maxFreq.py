# 1297. Maximum Number of Occurrences of a Substring
# https://leetcode.com/problems/maximum-number-of-occurrences-of-a-substring/description/
def maxFreq(s, maxLetters, minSize, maxSize):
    d = {}
    n= len(s)
    for i in range(n-minSize+1):
        for j in range(minSize, maxSize+1):
            print(s[i:i+j])


s = "aababcaab"
maxLetters = 2
minSize = 3
maxSize = 4

# s = "aaaa"
# maxLetters = 1
# minSize = 3
# maxSize = 3
#
# s = "abcde"
# maxLetters = 2
# minSize = 3
# maxSize = 3
print(maxFreq(s, maxLetters, minSize, maxSize))

# def maxFreq(s, maxLetters, minSize, maxSize):
#     d = {}
#     n =len(s)
#     for i in range(n):
#         for j in range(i, n+1):
#             temp = s[i:j]
#             if len(set(temp)) <= maxLetters and minSize <= len(temp):
#                 if temp not in d:
#                     d[temp] = 1
#                 else:
#                     d[temp] += 1
#     if len(d):
#         return max(d.values())
#     return 0
