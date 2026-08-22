# 290. Word Pattern
def wordPattern(pattern, s):
    pattern = list(pattern)
    s = s.split()
    if len(pattern) != len(s):
        return False
    if len(set(pattern)) != len(set(s)):
        return False
    d = {}
    for i in range(len(pattern)):
        if pattern[i] not in d:
            d[pattern[i]] = s[i]
        else:
            if d[pattern[i]] != s[i]:
                return False
    return True


# pattern = "abba"
# s = "dog cat cat dog"
# pattern = "abba"
# s = "dog cat cat fish"
# pattern = "aaaa"
# s = "dog cat cat dog"
# pattern = "abba"
# s = "dog dog dog dog" #Expected: False
pattern = "aba"
s = "cat cat cat dog"
print(wordPattern(pattern, s))
