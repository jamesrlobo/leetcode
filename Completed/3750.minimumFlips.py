# 3750. Minimum Number of Flips to Reverse Binary String
# Beats: 40.05%
def minimumFlips(n):
    s = bin(n)[2:]
    rev_s = s[::-1]
    if s == rev_s:
        return 0
    flips = 0
    for i in range(len(rev_s)):
        if rev_s[i] != s[i]:
            flips += 1
    return flips


n = 7
print(minimumFlips(n))
