# 3823. Reverse Letters Then Special Characters in a String
# https://leetcode.com/problems/reverse-letters-then-special-characters-in-a-string/description/
# Beats: 100.00%
def reverseByType(s):
    letters = []
    characters = []
    for i in range(len(s)):
        if s[i].isalpha():
            letters.append(s[i])
        else:
            characters.append(s[i])
    output = ""
    print(characters)
    # letters = letters[::-1]
    # characters = characters[::-1]
    for x in range(len(s)):
        if s[x].isalpha():
            output += letters.pop()
        else:
            output += characters.pop()
    return output


s = ")ebc#da@f("
s = "z"
s = "!@#$%^&*()"
print(reverseByType(s))
