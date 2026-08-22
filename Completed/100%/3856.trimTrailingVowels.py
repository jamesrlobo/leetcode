# 3856. Trim Trailing Vowels
# Beats: 100.00%
def trimTrailingVowels(s):
    s = [x for x in s]
    s = s[::-1]
    i = 0
    while i < len(s):
        if s[i] in "aeiou":
            s.pop(i)
            # print(s)
        else:
            break
    return "".join(s)[::-1]


s = "idea"
s = "day"
s = "aeiou"
print(trimTrailingVowels(s))
