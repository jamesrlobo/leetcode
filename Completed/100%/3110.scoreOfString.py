# 3110. Score of a String
# Beats: 100.00%
def scoreOfString(s):
    output = 0
    for i in range(len(s)-1):
        output += abs(ord(s[i]) - ord(s[i+1]))
    return output


# s = "hello"
s = "zaz"
print(scoreOfString(s))
