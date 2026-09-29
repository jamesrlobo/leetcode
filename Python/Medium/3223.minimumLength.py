# 3223. Minimum Length of String After Operations
# https://leetcode.com/problems/minimum-length-of-string-after-operations/description/
# Beats: 98.24%
def minimumLength(s):
    output = 0
    for i in set(s):
        if s.count(i) < 3:
            output += s.count(i)
        else:
            if s.count(i)%2 == 0:
                output += 2
            else:
                output += 1
    return output


s = "abaacbcbb"
s = "aa"
s = "ucvbutgkohgbcobqeyqwppbxqoynxeuuzouyvmydfhrprdbuzwqebwuiejoxsxdhbmuaiscalnteocghnlisxxawxgcjloevrdcj"
print(minimumLength(s))
