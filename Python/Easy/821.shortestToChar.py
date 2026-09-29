# 821. Shortest Distance to a Character
# Beats: 29.68%
def shortestToChar(s, c):
    c_index, output = [], []
    for i in range(len(s)):
        if s[i] == c:
            c_index.append(i)
    for j in range(len(s)):
        temp = []
        for k in c_index:
            temp.append(abs(j-k))
        output.append(min(temp))
    return output


# s = "loveleetcode"
# c = "e"
s = "aaab"
c = "b"
print(shortestToChar(s, c))
