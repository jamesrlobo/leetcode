#2529. Maximum Count of Positive Integer and Negative Integer
#Beats: 100.00%
def maximumCount(nums):
    neg, pos = 0 , 0
    for i in range(len(nums)):
        if nums[i] > 0:
            pos +=1
        elif nums[i] < 0:
            neg +=1
    return max(pos, neg)


nums = [-3,-2,-1,0,0,1,2]
print(maximumCount(nums))
