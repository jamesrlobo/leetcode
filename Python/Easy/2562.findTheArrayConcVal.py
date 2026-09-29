# 2562. Find the Array Concatenation Value
def findTheArrayConcVal(nums):
    concatenation = 0
    l = len(nums)
    if len(nums) == 1:
        return concatenation + nums[0]
    i = 0
    while i < l/2:
        string = ""
        # print(i, nums[i], nums[len(nums)-1-i])
        string += str(nums.pop(0))
        string += str(nums.pop())
        concatenation += int(string)
        # print(nums)
        if len(nums) == 0:
            return concatenation
        elif len(nums) == 1:
            return concatenation + nums[0]
        i==1


# nums = [7,52,2,4]
# nums = [5,14,13,8,12]
nums = [1]
print(findTheArrayConcVal(nums))
