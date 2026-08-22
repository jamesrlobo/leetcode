# 1991. Find the Middle Index in Array
# Beats: 100.00%
def findMiddleIndex(nums):
    preSum = 0
    for i in range(len(nums)):
        if preSum == sum(nums[i+1:]):
            return i
        preSum += nums[i]
    return -1


nums = [2,3,-1,8,4]
nums = [1,-1,4]
nums = [2,5]
print(findMiddleIndex(nums))

# for i in range(len(nums)):
#     # print(nums[:i], nums[i+1:])
#     # print(sum(nums[:i]), sum(nums[i+1:]))
#     if sum(nums[:i]) == sum(nums[i+1:]):
#         return i
# return -1
