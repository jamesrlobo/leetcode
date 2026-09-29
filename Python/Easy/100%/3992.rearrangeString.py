# 3992. Rearrange String to Avoid Character Pair
# https://leetcode.com/problems/rearrange-string-to-avoid-character-pair/description/
# Beats: 100%
def rearrangeString(s, x, y):
    t  = ""
    count_y = s.count(y)
    count_x = s.count(x)
    for i in range(len(s)):
        if s[i] != y and s[i] != x:
            t += s[i]
    return (y*count_y)+t+(x*count_x)


s = "aabc"
x = "a"
y = "c"
print(rearrangeString(s, x, y))

# Beats: 40.68%
# def rearrangeString(s, x, y):
#     letters = [ x for x in s]
#     if x < y:
#         letters = sorted(letters, reverse=True)
#     else:
#         letters = sorted(letters)
#     return "".join(letters)
