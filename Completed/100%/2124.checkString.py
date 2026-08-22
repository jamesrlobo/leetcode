# 2124. Check if All A's Appears Before All B's
# Beats:100.00%
def checkString(s):
    index_a = []
    index_b = []
    for i in range(len(s)):
        if s[i] == "a":
            index_a.append(i)
        else:
            index_b.append(i)
    if index_a == [] or index_b == []:
        return True
    if max(index_a) < min(index_b):
        return True
    else:
        return False


#s = "aaabbb"
#s = "abab"
s = "bbb"
print(checkString(s))
