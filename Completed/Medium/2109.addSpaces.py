# 2109. Adding Spaces to a String
# Beats: 94.12%
def addSpaces(s, spaces):
    output = []
    start = 0
    for i in range(len(spaces)):
        output.append(s[start:spaces[i]])
        start = spaces[i]
    output.append(s[start:])
    return " ".join(output)


s = "LeetcodeHelpsMeLearn"
spaces = [8,13,15]

s = "icodeinpython"
spaces = [1,5,7,9]

s = "spacing"
spaces = [0,1,2,3,4,5,6]
print(addSpaces(s, spaces))
