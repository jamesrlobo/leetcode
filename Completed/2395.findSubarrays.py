# 2395. Find Subarrays With Equal Sum
# https://leetcode.com/problems/find-subarrays-with-equal-sum/description/
# Beats: 8.24%
def findSubarrays(nums):
    total_sum = []
    for i in range(len(nums)-1):
        total = sum(nums[i:i+2])
        if total in total_sum:
            return True
        else:
            total_sum.append(total)
    return False


nums = [4,2,4]
nums = [1,2,3,4,5]
nums = [0,0,0]
print(findSubarrays(nums))
