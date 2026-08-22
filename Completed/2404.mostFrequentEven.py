# 2404. Most Frequent Even Element
# https://leetcode.com/problems/most-frequent-even-element/description/
# Beats: 5.00%
def mostFrequentEven(nums):
    output = -1
    count = 0
    for i in set(nums):
        if i%2 == 0:
            if nums.count(i) > count:
                output = i
                count = nums.count(i)
            elif nums.count(i) == count:
                output = min(i, output)
    return output


nums = [0,1,2,2,4,4,1]
nums = [4,4,4,9,2,4]
nums = [29,47,21,41,13,37,25,7]
nums = [0,1,2,0,0,0,2,4,4,1]
print(mostFrequentEven(nums))


# def mostFrequentEven(nums):
#     d = {}
#     for i in set(nums):
#         if i%2 == 0:
#             if nums.count(i) not in d:
#                 d[nums.count(i)] = [i]
#             else:
#                 d[nums.count(i)] += [i]
#     if len(d) > 0:
#         return min(d[max(d)])
#     return -1
