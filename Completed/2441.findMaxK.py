# 2441. Largest Positive Integer That Exists With Its Negative
def findMaxK(nums):
    result = []
    for i in nums:
        if i < 0 and abs(i) in nums:
            result.append(abs(i))
    if len(result) > 0:
        return max(result)
    else:
        return -1

# nums = [-1,10,6,7,-7,1]
nums = [-10,8,6,7,-2,-3]
print(findMaxK(nums))
