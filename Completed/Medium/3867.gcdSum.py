# 3867. Sum of GCD of Formed Pairs
# https://leetcode.com/problems/sum-of-gcd-of-formed-pairs/description/
# Beats: 5.39%
import math

def gcdSum(nums):
    n = len(nums)
    prefixGcd = []
    mx = nums[0]
    for i in range(n):
        mx = max(mx, nums[i])
        prefixGcd.append(math.gcd(nums[i], mx))
    prefixGcd = sorted(prefixGcd)
    ln = len(prefixGcd)
    output = 0
    x = 0
    while x < ln//2:
        print("prefixgcd:", prefixGcd, x)
        output += math.gcd(prefixGcd[0], prefixGcd[-1])
        prefixGcd.pop(-1)
        prefixGcd.pop(0)
        x+=1
    return output


nums = [2,6,4]
nums = [3,6,2,8]
nums = [8,38,33,32,28,20]
print(gcdSum(nums))
