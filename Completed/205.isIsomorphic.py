# 205. Isomorphic Strings
def isIsomorphic(s, t):
    d = {}
    for i, j in zip(s, t):
        if i not in d and j not in d.values():
            d[i] = j
        elif d.get(i) != j:
            return False
    return True

s = "paper"
t = "title"
# s = "egg"
# t = "add"
# s = "foo"
# t = "bar"
# s = "badc"
# t = "baba"
print(isIsomorphic(s,t))
