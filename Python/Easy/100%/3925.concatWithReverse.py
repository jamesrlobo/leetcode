# 3925. Concatenate Array With Reverse
# https://leetcode.com/problems/concatenate-array-with-reverse/description/
# Beats: 100.00%
def concatWithReverse(nums):
    ans = []
    ans.extend(nums)
    ans.extend(reversed(nums))
    return ans


nums = [1,2,3]
nums = [1]
print(concatWithReverse(nums))
