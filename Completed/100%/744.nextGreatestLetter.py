# 744. Find Smallest Letter Greater Than Target
# https://leetcode.com/problems/find-smallest-letter-greater-than-target/description/
# Beats: 100.00%
def nextGreatestLetter(letters, target):
    for i in letters:
        if ord(i) > ord(target):
            return i
    return letters[0]


letters = ["c","f","j"]
target = "a"

letters = ["c","f","j"]
target = "c"
print(nextGreatestLetter(letters, target))
