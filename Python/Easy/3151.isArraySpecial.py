# 3151. Special Array I
def isArraySpecial(nums):
    i = 1
    while i < len(nums):
        print(nums[i-1], nums[i])
        if nums[i-1]%2 == 0 and nums[i]%2 != 1:
            return False
        elif nums[i-1]%2 == 1 and nums[i]%2 != 0:
            return False
        i+=1
    return True

# nums = [4,3,1,6]
# nums = [1]
# nums = [2,1,4]
nums = [2]
print(isArraySpecial(nums))
