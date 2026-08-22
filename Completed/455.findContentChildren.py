# 455. Assign Cookies (Copied from soltuions)
# Beats: 37.14%
def findContentChildren(g, s):
    g.sort()
    s.sort()
    count = 0
    i, j = 0, 0
    while i < len(g) and j < len(s):
        if s[j] >= g[i]:
            count += 1
            i+=1
        j+=1
    return count


g = [1,2,3]
s = [1,1]

g = [1,2]
s = [1,2,3]
print(findContentChildren(g,s))
