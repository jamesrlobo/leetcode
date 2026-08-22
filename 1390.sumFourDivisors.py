# https://leetcode.com/problems/four-divisors/description/?envType=daily-question&envId=2026-01-04
import math


def sumFourDivisors(nums):
    output = 0
    for i in set(nums):
        divisors = [x for x in range(1, int(math.sqrt(i))+1) if i%x == 0]
        print(divisors)
        if len(divisors) == 4:
            output += (sum(divisors) * nums.count(i))
    return output



nums = [21,4,7]
# nums = [21,21]
print(sumFourDivisors(nums))
