# 3637. Trionic Array I
# Beats: 100.00%
def isTrionic(nums):
    for i in range(1, len(nums)-1):
        if nums[i] > nums[i+1]:
            break
    first = nums[:i+1]
    if len(first) < 1 or len(first) != len(set(first)):
        return False
    if first != sorted(first):
        return False
    for j in range(i, len(nums)-1):
        if nums[j] < nums[j+1]:
            break
    second = nums[i:j+1]
    if len(second) < 2 or len(second) != len(set(second)):
        return False
    if second != sorted(second, reverse=True):
        return False
    third = nums[j:]
    if third != sorted(third) or len(third) < 1:
        return False
    if len(third) != len(set(third)):
        return False
    return True


nums = [1,3,5,4,2,6] #True
nums = [2,1,3] #False
nums = [1,2,3] #False
nums = [8,8,2,6] #False
nums = [5,9,1,7] #True
nums = [1,6,6,3,7] #False
nums = [8,6,3,5] #False
print(isTrionic(nums))
