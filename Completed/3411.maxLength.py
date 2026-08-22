# 3411. Maximum Subarray With Equal Products
# https://leetcode.com/problems/maximum-subarray-with-equal-products/description/
# Beats: 26.18%
import math
def maxLength(nums):
   n = len(nums)
   output = []
   for i in range(n):
      for j in range(i, n+1):
         # print(nums[i:j])
         if len(nums[i:j]) > 1:
            temp = nums[i:j]
            prod_arr = math.prod(temp)
            # print("prod_arr:", prod_arr)
            lcm_arr = math.lcm(*temp)
            # print("lcm_arr:", lcm_arr)
            gcd_arr = math.gcd(*temp)
            # print("gcd_arr:", gcd_arr)
            if prod_arr == lcm_arr*gcd_arr:
               output.append(len(temp))
   if len(output) > 0:
      return max(output)
   return 0

nums = [1,2,1,2,1,1,1]
nums = [2,3,4,5,6]
nums = [1,2,3,1,4,5,1]
print(maxLength(nums))
