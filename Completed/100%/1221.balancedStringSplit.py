# 1221. Split a String in Balanced Strings
# Beats: 100.00%
def balancedStringSplit(s):
    count, output = 0, 0
    for i in range(len(s)):
        if s[i] == "R":
            count += 1
        else:
            count -= 1
        if count == 0:
            output += 1
    return output


# s = "RLRRLLRLRL"
# s = "RLRRRLLRLL"
s = "LLLLRRRR"
print(balancedStringSplit(s))
