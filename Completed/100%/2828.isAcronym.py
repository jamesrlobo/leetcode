# 2828. Check if a String Is an Acronym of Words
# https://leetcode.com/problems/check-if-a-string-is-an-acronym-of-words/description/
# Beats: 100.00%
def isAcronym(words, s):
    acronym = ""
    for i in words:
        acronym += i[0]
    if acronym == s:
        return True
    return False


words = ["alice","bob","charlie"]
s = "abc"

words = ["an","apple"]
s = "a"

words = ["never","gonna","give","up","on","you"]
s = "ngguoy"
print(isAcronym(words, s))
