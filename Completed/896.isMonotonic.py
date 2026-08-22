# 896. Monotonic Array
# Beats: 86.49%
def isMonotonic(nums):
    if len(nums) == 1:
        return True
    l = len(nums)-1
    for i in range(1, len(nums)):
        if nums[i] < nums[i-1]:
            break
        if i == l:
            return True
    for j in range(1, len(nums)):
        if nums[i] > nums[i+1]:
            break
        if i == l:
            return True
    return False


nums = [1,2,2,3]
nums = [9]
print(isMonotonic(nums))
