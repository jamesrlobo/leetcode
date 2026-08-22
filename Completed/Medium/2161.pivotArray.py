# 2161. Partition Array According to Given Pivot
# https://leetcode.com/problems/partition-array-according-to-given-pivot/description/
Beats: 97.42%
def pivotArray(nums, pivot):
    smaller, common, larger = [], [], []
    for i in nums:
        if i == pivot:
            common.append(i)
        elif i > pivot:
            larger.append(i)
        else:
            smaller.append(i)
    return smaller+common+larger


nums = [9,12,5,10,14,3,10]
pivot = 10
# nums = [-3,4,3,2]
# pivot = 2
print(pivotArray(nums, pivot))


# Beats: 97.42%
# def pivotArray(nums, pivot):
#     smaller, common, larger = [], [], []
#     for i in nums:
#         if i == pivot:
#             common.append(i)
#         elif i > pivot:
#             larger.append(i)
#         else:
#             smaller.append(i)
#     return smaller+common+larger

# Beats: 92.47%
# def pivotArray(nums, pivot):
#     smaller, larger = [], []
#     count = 0
#     for i in nums:
#         if i == pivot:
#             count += 1
#         elif i < pivot:
#             smaller.append(i)
#         else:
#             larger.append(i)
#     return smaller + [pivot]*count + larger
