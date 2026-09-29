# 242. Valid Anagram
# https://leetcode.com/problems/valid-anagram/description/
# Beats: 100.00%
def isAnagram(s, t):
    if len(s) != len(t):
        return False
    for i in set(s):
        if s.count(i) != t.count(i):
            return False
    return True


s = "anagram"
t = "nagaram"

s = "rat"
t = "car"
print(isAnagram(s, t))
