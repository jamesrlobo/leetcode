# https://leetcode.com/problems/minimum-absolute-difference-between-two-values/
# 3880. Minimum Absolute Difference Between Two Values
# Beats: -%
def minAbsoluteDifference(nums):
    output = []
    for i in range(len(nums)):
        if nums[i] == 1:
            for j in range(len(nums)):
                if nums[j] == 2: #and i != j:
                    output.append(abs(i-j))
    if output:
        return min(output)
    return -1


nums = [1,0,0,2,0,1]
# nums = [1,0,1,0]
print(minAbsoluteDifference(nums))
