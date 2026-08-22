# 594. Longest Harmonious Subsequence
# Beats: 5.03%
def findLHS(nums):
    output = 0
    nums = sorted(nums)
    set_nums = sorted(list(set(nums)))
    print(set_nums)
    for i in range(len(set_nums)-1):
        if (abs(set_nums[i] - set_nums[i+1])) == 1:
            temp = [x for x in nums if x == set_nums[i] or x == set_nums[i+1]]
            if len(temp) > output:
                output = len(temp)
    return output


nums = [1,3,2,2,5,2,3,7]
# nums = [1,2,3,4]
# nums = [1,1,1,1]
nums = [62,27,90,59,63,26,40,26,72,36]
print(findLHS(nums))


# Beats: 5.03%
# from collections import Counter
# def findLHS(nums):
#     output = []
#     nums = sorted(nums)
#     cntr = Counter(nums)
#     for i in cntr:
#         temp = 0
#         for j in cntr:
#             if i < j and abs(i - j) == 1:
#                 temp = cntr[i] + cntr[j]
#         output.append(temp)
#     return max(output)
#
#
# nums = [1,3,2,2,5,2,3,7]
# print(findLHS(nums))
