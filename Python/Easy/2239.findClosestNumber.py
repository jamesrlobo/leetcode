# 2239. Find Closest Number to Zero
def findClosestNumber(nums):
    positive, negative = [], []
    for i in range(len(nums)):
        # print("Number", nums[i])
        if nums[i] >= 0:
            positive.append(nums[i])
        else:
            negative.append(nums[i]-0)
    if positive == []:
        print(max(negative))
        return max(negative)
    elif negative == []:
        print(min(positive))
        return min(positive)
    else:
        print(min(positive), max(negative))
        if abs(min(positive)) > abs(max(negative)):
            return max(negative)
        else:
            return min(positive)


# nums = [-4,-2,1,4,8]
# nums = [2,-1,1]
# nums = [-100000,-100000] #Expected: -100000
nums = [2,1,1,-1,100000] #Expected: 1
print(findClosestNumber(nums))
