def isPalindrome(s):
    new = ""
    for i in range(len(s)):
        if s[i].isalnum():
            new += s[i].lower()
    if new == new[::-1]:
        return True
    return False


# s = "A man, a plan, a canal: Panama"
# s = "race a car"
s = "0P"
print(isPalindrome(s))
