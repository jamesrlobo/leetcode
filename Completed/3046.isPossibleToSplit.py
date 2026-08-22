# 3046. Split the Array
def isPossibleToSplit(nums):
    for i in nums:
        if nums.count(i) > 2:
            return False
    return True


nums = [1,1,2,2,3,4]
# nums = [1,1,1,1]
print(isPossibleToSplit(nums))
