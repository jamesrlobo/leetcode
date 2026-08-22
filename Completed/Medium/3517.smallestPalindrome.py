# 3517. Smallest Palindromic Rearrangement I
# https://leetcode.com/problems/smallest-palindromic-rearrangement-i/description/
# Beats: 97.70%
def smallestPalindrome(s):
    alphabets = sorted(set(s))
    output = []
    mid = ""
    for i in alphabets:
        for x in range(s.count(i)//2):
            output.append(i)
        if s.count(i)%2 != 0:
            mid = i
    output = "".join(output)
    return output+mid+output[::-1]


s = "babab"
s = "daccad"
# s = "z"
s = "yey"
s = "jjejj"
print(smallestPalindrome(s))

# Beats: 29.03%
# def smallestPalindrome(s):
#     n = len(s)
#     if n%2 == 0:
#         return "".join((sorted(s[:n//2]) + sorted(s[:n//2])[::-1]))
#     middle = ""
#     output = []
#     for i in sorted(set(s)):
#         if s.count(i)%2 != 0:
#             middle = i
#             for x in range(s.count(i)//2):
#                 output.append(i)
#         else:
#             for x in range(s.count(i)//2):
#                 output.append(i)
#     output = "".join(output)
#     return output+middle+output[::-1]

# Beats: 5.07%
# def smallestPalindrome(s):
#     alphabets = sorted(set(s))
#     first = ""
#     middle = ""
#     second = ""
#     for i in alphabets:
#         if s.count(i)%2 == 0:
#             for x in range(s.count(i)//2):
#                 first += i
#                 second = i + second
#         else:
#             middle = i
#             for x in range(s.count(i)//2):
#                 first += i
#                 second = i+ second
#     return first+middle+second
