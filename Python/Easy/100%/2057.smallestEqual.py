#2057. Smallest Index With Equal Value
#Beats: 100%
def smallestEqual(nums):
    output = []
    for i in range(len(nums)):
        if i%10 == nums[i]:
            output.append(i)
    if len(output) > 0:
        return min(output)
    else:
        return -1


# nums = [0,1,2]
# nums = [4,3,2,1]
nums = [1,2,3,4,5,6,7,8,9,0]
print(smallestEqual(nums))
