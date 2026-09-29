# 3194. Minimum Average of Smallest and Largest Elements
def minimumAverage(nums):
    l = len(nums)/2
    nums.sort()
    averages = []
    i = 0
    while i < l:
        # print("i:",i)
        averages.append((nums[0] + nums[len(nums)-1])/2)
        nums.remove(nums[0])
        nums.remove(nums[len(nums)-1])
        # print(nums)
        i+=1
    return min(averages)


# nums = [7,8,3,4,15,13,4,1]
# nums = [1,9,8,3,10,5]
nums = [1,2,3,7,8,9]
print(minimumAverage(nums))
