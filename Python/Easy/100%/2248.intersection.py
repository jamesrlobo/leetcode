# 2248. Intersection of Multiple Arrays
# Beats: 100.00%
def intersection(nums):
    output = nums[0]
    for i in range(1, len(nums)):
        temp = (set(output) & set(nums[i]))
        output = temp
    return list(output)

# nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]
nums = [[1,2,3],[4,5,6]]
print(intersection(nums))
