# 674. Longest Continuous Increasing Subsequence
# Beats: 11.19%
def findLengthOfLCIS(nums):
    if len(nums) == 1:
        return 1
    i = 0
    n = len(nums)
    output = []
    while i != n-1:
        temp = [nums[i]]
        for j in range(i, len(nums)-1):
            if nums[j] < nums[j+1]:
                temp.append(nums[j+1])
            else:
                break
        output.append(len(temp))
        i+=1
    if len(output) != 0:
        return max(output)
    else:
        return 0


nums = [1,3,5,4,7]
nums = [2,2,2,2,2]
nums = [1]

print(findLengthOfLCIS(nums))
