# 2221. Find Triangular Sum of an Array
# Beats: 60.99%
def triangularSum(nums):
    if len(nums) == 1:
        return sum(nums)
    while len(nums) != 1:
        temp = []
        for i in range(len(nums)-1):
            temp.append((nums[i]+nums[i+1])%10)
        nums = temp
        # print(nums)
    return sum(nums)


nums = [1,2,3,4,5]
nums = [5]
print(triangularSum(nums))
