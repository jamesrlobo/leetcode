# 521. Longest Uncommon Subsequence I
# Beats: 100.00%
def findLUSlength(a: str, b: str) -> int:
    if a == b:
        return -1
    else:
        return max(len(a), len(b))


a = "aba"
b = "cdc"
print(findLUSlength(a,b))
