# 1576. Replace All ?'s to Avoid Consecutive Repeating Characters
# Beats: 100.00%
def modifyString(s):
    if s == "?":
        return "a"
    s = list(s)
    for i in range(len(s)-1):
        if s[i] == "?":
            if s[i-1] != "a" and s[i+1] != "a":
                s[i] = "a"
            elif s[i-1] != "b" and s[i+1] != "b":
                s[i] = "b"
            elif s[i-1] != "c" and s[i+1] != "c":
                s[i] = "c"
    if s[-1] == "?":
        if s[-2] == "z":
            s[-1] = chr(ord(s[-2])-1)
        else:
            s[-1] = chr(ord(s[-2])+1)
    return "".join(s)


# s = "?zs"
# s = "ubv?w"
# s = "j?qg??b"
# s = "ubv?w"
# s = "a?e"
# s = "b?h"
s = "??"
print(modifyString(s))
