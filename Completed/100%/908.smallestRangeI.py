# 908. Smallest Range I
# https://leetcode.com/problems/smallest-range-i/description/
# Beats: 100.00%
def smallestRangeI(nums, k):
    mx = max(nums)
    mn = min(nums)
    result = (mx - k) - (mn + k)
    return max(0, result)


nums = [1]
k = 0

# nums = [1,3,6]
# k = 3
#
# nums = [0,10]
# k = 2
print(smallestRangeI(nums, k))

# def smallestRangeI(nums, k):
#     print("Turn:", k)
#     mx = max(nums)
#     mn = min(nums)
#     while k > 0:
#         mx -= 1
#         mn += 1
#         if mn > mx or mx == mn:
#             return 0
#         k -= 1
#     return mx - mn
