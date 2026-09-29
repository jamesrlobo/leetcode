# 628. Maximum Product of Three Numbers -> Checked from solutions
# Beats: 97.36%
import heapq


def maximumProduct(nums):
    max1, max2, max3 = heapq.nlargest(3, nums)
    min1, min2 = heapq.nsmallest(2, nums)
    return max(max1*max2*max3, min1*min2*max1)


# nums = [1,2,3,4]
# nums = [1,2,3]
# nums = [-1,-2,-3]
nums = [-100,-98,-1,2,3,4] #Expected: 39200
print(maximumProduct(nums))
