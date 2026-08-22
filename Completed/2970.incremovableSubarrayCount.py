# 2970. Count the Number of Incremovable Subarrays I
# https://leetcode.com/problems/count-the-number-of-incremovable-subarrays-i/description/
# Beats: 10.97%
def incremovableSubarrayCount(nums):
    count = 0
    n = len(nums)
    for i in range(n):
        for j in range(i, n+1):
            if len(nums[i:j]) > 0:
                # print(nums[i:j])
                temp = nums[:i] + nums[j:]
                if len(temp) == len(set(temp)):
                    if temp == sorted(temp) and len(temp) == len(set(temp)):
                        count += 1
    return count


nums = [1,2,3,4]
# nums = [6,5,7,8]
# nums = [8,7,6,6]
print(incremovableSubarrayCount(nums))
