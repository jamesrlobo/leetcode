# 3727. Maximum Alternating Sum of Squares
# https://leetcode.com/problems/maximum-alternating-sum-of-squares/description/
# Beats: 71.98%
def maxAlternatingSum(self, nums: List[int]) -> int:
    n = len(nums)
    new_nums = [(abs(x)**2) for x in nums]
    new_nums = sorted(new_nums)
    # print(new_nums)
    mid = n//2
    return sum(new_nums[mid:]) - sum(new_nums[:mid])
