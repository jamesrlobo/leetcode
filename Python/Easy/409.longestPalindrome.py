# 409. Longest Palindrome
# Beats: 14.54%
# Step : 1) Frequency of characters
# Step :2) Max odd frequency of character
# Step: 3) We can form palindrome , if all characters have an even frequency count or a single character has an odd frequency count (which can be placed in the middle of the palindrome), it is possible to form a palindrome string.
# Step:4) If you find a characters with frequency odd but less than max odd then round off to previous even
def longestPalindrome(s):
    if len(s) == 1:
        return 1
    count = 0
    d = {}
    odd = []
    for i in set(s):
        d[i] = s.count(i)
        if s.count(i)%2 != 0:
            odd.append(s.count(i))
    # print(d)
    if len(odd) > 0:
        maximum_odd = max(odd)
    valid = True
    for j in d:
        if d[j]%2 == 0:
            count += d[j]
        elif d[j]%2 != 0 and valid == True:
            count += d[j]
            valid = False
        else:
            count += d[j]-1
    return count



s = "abccccdd"
s = "bb"
print(longestPalindrome(s))
