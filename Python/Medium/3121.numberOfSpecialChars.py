# 3121. Count the Number of Special Characters II
# https://leetcode.com/problems/count-the-number-of-special-characters-ii/description/
# Beats: 5.30%
def numberOfSpecialChars(word):
    count = 0
    for i in set(word):
        if i.islower():
            lower_index, caps_index = [], []
            for j in range(len(word)):
                if word[j] == i:
                    lower_index.append(j)
                elif word[j] == i.capitalize():
                    caps_index.append(j)
            if len(lower_index) > 0 and len(caps_index) > 0:
                if max(lower_index) < min(caps_index):
                    count += 1
    return count


word = "aaAbcBC"
# word = "abc"
# word ="cCceDC"
print(numberOfSpecialChars(word))
