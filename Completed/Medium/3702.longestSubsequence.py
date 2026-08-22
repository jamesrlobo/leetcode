# 3702. Longest Subsequence With Non-Zero Bitwise XOR
# https://leetcode.com/problems/longest-subsequence-with-non-zero-bitwise-xor/description/
# Beats: 42.74% [Copied from solutions]
def longestSubsequence(nums):
    n = len(nums)
    totalXor = 0
    allZero = True
    for x in nums:
        totalXor ^= x
        if x > 0:
            allZero = False
    if totalXor > 0:
        return n
    if not allZero:
        return n-1
    return 0


nums = [1,2,3]
# nums = [6,0]
nums = [1,6,6]
# nums = [91,8,34,103,72,102,102,46,102,140,118,35]
# nums = [129,364,235,312,170,379,275,244,23,68,292,157,315,124,215,70,365,65,266,301]
print(longestSubsequence(nums))

# def longestSubsequence(nums):
#     subsequence = []
#     output = []
#     for r in range(len(nums)+1):
#         for comb in combinations(nums, r):
#             subsequence.append(list(comb))
#     for item in subsequence:
#         result = 0
#         for i in item:
#             result ^= i
#         if result != 0:
#             output.append(len(item))
#     return max(output)
