# 485. Max Consecutive Ones
def findMaxConsecutiveOnes(nums):
    count_list = []
    count = 0
    for i in range(len(nums)):
        if nums[i] == 1:
            count +=1
        else:
            count_list.append(count)
            count = 0
    count_list.append(count)
    return max(count_list)

# nums = [1,1,0,1,1,1]
nums = [1,0,1,1,0,1]
print(findMaxConsecutiveOnes(nums))
