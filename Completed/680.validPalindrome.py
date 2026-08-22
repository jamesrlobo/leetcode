# 680. Valid Palindrome II
def validPalindrome(s):
    if s == s[::-1]:
        return True
    a = list(s)
    b = list(s)[::-1]
    i = 0
    while i < len(s):
        if a[i] != b[i]:
            position = i
            break
        i+=1
    a.pop(position)
    if "".join(a) == "".join(a)[::-1]:
        return True
    b.pop(position)
    if "".join(b) == "".join(b)[::-1]:
        return True
    return False


# s = "abca"
# s = "aba"
# s = "abc"
s = "cbbcc"
print(validPalindrome(s))
