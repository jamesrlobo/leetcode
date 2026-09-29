# 4006. Count Valid Prefixes
# https://leetcode.com/problems/count-valid-prefixes/description/
# Beats: 68.60%
def countValidPrefixes(s):
    noOfZeroes, noOfOnes, count = 0, 0, 0
    for i in s:
        if i == "0":
            noOfZeroes += 1
        else:
            noOfOnes += 1
        if abs(noOfZeroes - noOfOnes) <= 1:
            count += 1
    return count


s = "00101"
s = "101"
print(countValidPrefixes(s))

# Beats: 68.60%
# def countValidPrefixes(s):
#     n = len(s)
#     noOfZeroes, noOfOnes, count = 0, 0, 0
#     for i in range(n):
#         if s[i] == "0":
#             noOfZeroes += 1
#         else:
#             noOfOnes += 1
#         if abs(noOfZeroes - noOfOnes) <= 1:
#             count += 1
#         print(noOfZeroes, noOfOnes, count)
#     return count
