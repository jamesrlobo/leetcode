# 4097. Minimum Value of Merged Integers
# https://leetcode.com/problems/minimum-value-of-merged-integers/
# Beats: 22.57%
def minMergedInteger(self, nums: list[int]) -> int:
    n = len(nums)
    output = int(str(nums[0])+str(nums[1]))
    i = 1
    while i <= n:
        s = str(nums[i-1])+str(nums[i])
        output = min(output, int(s))
        i+=2
    return output
