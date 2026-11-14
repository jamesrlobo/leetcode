# 1390. Four Divisors
# https://leetcode.com/problems/four-divisors/description/
# Beats: 5.03%
import math


def sumFourDivisors(nums):
    output = 0
    for num in nums:
        divisors = [1, num]
        i = 2
        # print(math.sqrt(num))
        while i <= int(math.sqrt(num)):
            if num%i == 0:
                divisors.append(i)
                if num//i not in divisors:
                    divisors.append(num//i)
            i+= 1
        if len(divisors) == 4:
            output += sum(divisors)
    return output



nums = [21,4,7]
# nums = [21,21]
print(sumFourDivisors(nums))
