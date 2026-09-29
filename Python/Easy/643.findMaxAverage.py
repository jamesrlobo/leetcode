# 643. Maximum Average Subarray I
# https://leetcode.com/problems/maximum-average-subarray-i/
#Beats: 92.44%
def findMaxAverage(nums, k):
    n = len(nums)
    start = 0
    end = start + k
    temp = sum(nums[start:end])
    output = temp
    while start < n-k:
        temp -= nums[start]
        temp += nums[end]
        output = max(output, temp)
        start += 1
        end = start + k
    return output/k


nums = [1,12,-5,-6,50,3]
k = 4
nums = [5]
k = 1
nums = [0,1,1,3,3]
k = 4
nums = [4,0,4,3,3]
k = 5
print(findMaxAverage(nums, k))
