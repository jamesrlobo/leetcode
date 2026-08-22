# 541. Reverse String II
def reverseStr(s,k):
    res = ""
    i, count = 0, 0
    while i < len(s):
        if count%2 == 0:
            res += (s[i:i+k][::-1])
            count += 1
        else:
            res += s[i:i+k]
            count += 1
        i+=k
    return res


# s = "abcdefg"
# k = 2
# s = "abcd"
# k = 2
s = "abcdef"
k = 3
print(reverseStr(s,k))
