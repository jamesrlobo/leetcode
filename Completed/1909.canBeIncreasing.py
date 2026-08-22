#1909. Remove One Element to Make the Array Strictly Increasing
#Beats: 5.64%
def canBeIncreasing(nums):
    temp = []
    for i in range(len(nums)):
        # print("No. to be popped:", nums[i])
        temp.extend(nums)
        temp.pop(i)
        # print(temp)
        for j in range(len(temp)-1):
            if temp[j] > temp[j+1] or temp[j] == temp[j+1]:
                break
        else:
            print("Sorted:", temp)
            return True
        temp = []
    return False

# nums = [1,2,10,5,7]
# nums = [2,3,1,2]
# nums = [1,1,1]
# nums = [1,2,3]
nums = [1,1]
print(canBeIncreasing(nums))
