# 2460. Apply Operations to an Array
def applyOperations(nums):
    i = 0
    while i < len(nums)-1:
        if nums[i] == nums[i+1]:
            nums[i] = nums[i]*2
            nums[i+1] = 0
            i+=1
        else:
            i+=1
    count = nums.count(0)
    while 0 in nums:
        nums.remove(0)
    for x in range(count):
        nums.append(0)
    return nums


# nums = [1,2,2,1,1,0]
# nums = [0,1]
nums = [847,847,0,0,0,399,416,416,879,879,206,206,206,272]
print(applyOperations(nums))
