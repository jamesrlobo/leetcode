# 4038. Count Integers Appearing in a Single Block
# https://leetcode.com/problems/count-integers-appearing-in-a-single-block/description/
# Beats: 100.00%
def countSpecialIntegers(nums):
    n = len(nums)
    d = {}
    output = 0
    for i in range(n):
        if nums[i] not in d:
            d[nums[i]] = [i]
        else:
            d[nums[i]] += [i]
    for x in set(nums):
        if nums.count(x) == (d[x][-1] - d[x][0] + 1):
            output += 1
    return output


nums = [1,2,2,1]
print(countSpecialIntegers(nums))
