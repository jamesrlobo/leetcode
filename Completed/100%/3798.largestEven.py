# 3798. Largest Even Number
# Beats: 100.00%
def largestEven(s):
    s = int(s)
    while s%2 != 0:
        s = s//10
    if s == 0:
        return ""
    else:
        return s


s = "1112"
s = "221"
s = "1"
print(largestEven(s))
