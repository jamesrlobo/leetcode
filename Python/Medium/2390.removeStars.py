# 2390. Removing Stars From a String
#Beats: 18.80%
def removeStars(s):
    output = []
    for i in range(len(s)):
        if s[i] != "*":
            output.append(s[i])
        else:
            output.pop()
    return "".join(output)


s = "leet**cod*e"
# s = "erase*****"
print(removeStars(s))
