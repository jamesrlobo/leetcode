# 942. DI String Match
# Beats: 71.44%
def diStringMatch(s):
    low, high = 0, len(s)
    perm = []
    for i in range(len(s)):
        if s[i] == "I":
            perm.append(low)
            low += 1
        else:
            perm.append(high)
            high -= 1
    perm.append(low)
    return perm


s = "IDID"
print(diStringMatch(s))
