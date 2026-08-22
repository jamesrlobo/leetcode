# 1848. Minimum Distance to the Target Element
# https://leetcode.com/problems/minimum-distance-to-the-target-element/description/
# Beats: 100.00%
def getMinDistance(nums, target, start):
    output = []
    for i in range(len(nums)):
        if nums[i] == target:
            output.append(abs(i-start))
    return min(output)


nums = [1,2,3,4,5]
target = 5
start = 3

nums = [1]
target = 1
start = 0

nums = [1,1,1,1,1,1,1,1,1,1]
target = 1
start = 0

nums  = [1,1,1,1,1,1,1,1,1,1]
target = 1
start = 9

nums = [5,3,6]
target = 5
start = 2
print(getMinDistance(nums, target, start))
