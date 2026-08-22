# 697. Degree of an Array
# Beats: 5.02%
def findShortestSubArray(nums):
    d = {}
    output = []
    for x in set(nums):
        if nums.count(x) not in d:
            d[nums.count(x)] = [x]
        else:
            d[nums.count(x)] += [x]
    maximum = d[max(d)]
    print(maximum)
    for i in maximum:
        index = []
        for j in range(len(nums)):
            if i == nums[j]:
                index.append(j)
        output.append(max(index)-min(index)+1)
    return min(output)


nums = [1,2,2,3,1]
nums = [1,2,2,3,1,4,2]
print(findShortestSubArray(nums))

# d = {}
# output = []
# for x in set(nums):
#     if nums.count(x) not in d:
#         d[nums.count(x)] = [x]
#     else:
#         d[nums.count(x)] += [x]
# maximum = d[max(d)]
# # print(maximum)
# for k in maximum:
#     for i in range(len(nums)):
#         for j in range(i, len(nums)+1):
#             if nums[i:j].count(k) == nums.count(k):
#                 output.append(len(nums[i:j]))
# return min(output)
