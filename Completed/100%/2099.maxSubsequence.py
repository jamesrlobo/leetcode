# 2099. Find Subsequence of Length K With the Largest Sum
# https://leetcode.com/problems/find-subsequence-of-length-k-with-the-largest-sum/description/
# Beats: 100.00% [Copied from comments]
def maxSubsequence(nums):
    sorted_nums = sorted(enumerate(nums), key=lambda x: x[1])
    res = [x for i, x in sorted(sorted_nums[-k:])]
    return res


nums = [2,1,3,3]
k = 2
nums = [-1,-2,3,4]
k = 3
print(maxSubsequence(nums))
