# 3982. Sum of Integers with Maximum Digit Range
# https://leetcode.com/problems/sum-of-integers-with-maximum-digit-range/description/
# Beats: 88.48%
def maxDigitRange(nums):
    d = {}
    n = len(nums)
    for i in range(n):
        rng = int(max(str(nums[i]))) - int(min(str(nums[i])))
        if rng not in d:
            d[rng] = int(nums[i])
        else:
            d[rng] += int(nums[i])
    return d[max(d)]


nums = [5724,111,350]
nums = [90,900]
nums = [76207,65921]
print(maxDigitRange(nums))


# d = {}
# n= len(nums)
# for i in range(n):
#     temp = []
#     for ch in str(nums[i]):
#         temp.append(int(ch))
#     rnge = max(temp) - min(temp)
#     if rnge not in d:
#         d[rnge] = int(nums[i])
#     else:
#         d[rnge] += int(nums[i])
# print(d)
# return d[max(d)]
