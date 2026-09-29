# 3407. Substring Matching Pattern
# https://leetcode.com/problems/substring-matching-pattern/description/
# Beats: 100.00%
def hasMatch(s, p):
    parts = p.split("*")
    # print(parts)
    part1 = parts[0]
    part2 = parts[1]
    l = len(part1)
    for i in range(len(s)-l+1):
        # print(s[i:i+l])
        if s[i:i+l] == part1:
            temp = i+l
            break
    else:
        return False
    if part2 in s[temp:]:
        return True
    return False


s = "leetcode"
p = "ee*e"

s = "car"
p = "c*v"

s = "luck"
p = "u*"
print(hasMatch(s, p))
