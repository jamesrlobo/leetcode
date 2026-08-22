# 152. Maximum Product Subarray
# https://leetcode.com/problems/maximum-product-subarray/description/
import math


def maxProduct(nums):
    if len(nums) == 1:
        return nums[0]
    subsets = [0]
    first = 0
    neg = False
    for i in range(len(nums)):
        if nums[i] == 0:
            if not neg:
                # subsets.append(math.prod(nums[first:i]))
                subsets.append(nums[first:i])
            else:
                # subsets.append(math.prod(nums[first:neg_pos]))
                # subsets.append(math.prod(nums[neg_pos+1:i]))
                subsets.append(nums[first:neg_pos])
                subsets.append(nums[neg_pos+1:i])
            first = i+1
        elif nums[i] < 0:
            neg_pos = i
            if not neg:
                neg = True
            else:
                neg = False
    print("here:", first, neg_pos)
    if neg == True:
        # subsets.append(math.prod(nums[first:neg_pos]))
        # subsets.append(math.prod(nums[neg_pos+1:]))
        subsets.append(nums[first:neg_pos])
        subsets.append(nums[neg_pos+1:])
    return subsets


nums = [2,3,-2,4]
nums = [-2,0,-1]
print(maxProduct(nums))
