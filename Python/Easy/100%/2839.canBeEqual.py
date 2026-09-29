# 2839. Check if Strings Can be Made Equal With Operations I
# Beats: 100.00%
def canBeEqual(s1, s2):
    original =s1
    if (s1[2]+s1[1]+s1[0]+s1[3]) == s2:
        return True
    else:
        s1 = (s1[2]+s1[1]+s1[0]+s1[3])
    if s1[0]+s1[3]+s1[2]+s1[1] == s2:
        return True
    else:
        s1 = original
    if (s1[0]+s1[3]+s1[2]+s1[1]) ==  s2:
        return True
    else:
        s1 = (s1[0]+s1[3]+s1[2]+s1[1])
    if (s1[2]+s1[1]+s1[0]+s1[4]) == s2:
        return True
    return False

# s1 = "abcd"
# s2 = "cdab"
# s1 = "abcd"
# s2 = "dacb"
s1 = "bnxw"
s2 = "bwxn"
print(canBeEqual(s1, s2))
