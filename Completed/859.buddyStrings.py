# 859. Buddy Strings (Copied from solutions)
#Beats: 45.23%
def buddyStrings(s, goal):
    n = len(s)
    if len(goal) != n:
        return False
    if s == goal:
        temp = set(s)
        return len(temp) < len(goal)
    i = 0
    j = n - 1
    while i < j and s[i] == goal[i]:
        i += 1
    while j >= 0 and s[j] == goal[j]:
        j -= 1
    if i < j:
        s_list = list(s)
        s_list[i], s_list[j] = s_list[j], s_list[i]
        s = ''.join(s_list)
    return s == goal


s = "aaaaaaabc"
goal = "aaaaaaacb"
# s = "ab"
# goal = "ba"
# s = "ab"
# goal = "ab"
# s = "aa"
# goal = "aa"
# s = "abcd"
# goal = "badc"
print(buddyStrings(s, goal))
