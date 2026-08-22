# 3707. Equal Score Substrings
# Beats: 8.73%
def scoreBalance(s):
    for i in range(1, len(s)):
        lhs, rhs = 0, 0
        for x in s[:i]:
            lhs += ord(x)-96
        for y in s[i:]:
            rhs += ord(y)-96
        if lhs == rhs:
            return True
    return False


# s = "adcb"
s = "bace"
print(scoreBalance(s))
