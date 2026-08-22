# 3794. Reverse String Prefix
# Beats: 100.00%
def reversePrefix(s, k):
    # print(s[:k][::-1])
    # print(s[k:])
    return (s[:k][::-1]) + (s[k:])


s = "abcd"
k = 2

s = "xyz"
k = 3

s = "hey"
k = 1
print(reversePrefix(s, k))
