# 2810. Faulty Keyboard
# https://leetcode.com/problems/faulty-keyboard/description/
# Beats: 100.00%
def finalString(s):
    output = ""
    for i in s:
        if i != "i":
            output += i
        else:
            output = output[::-1]
    return output


s = "string"
s = "poiinter"
print(finalString(s))
