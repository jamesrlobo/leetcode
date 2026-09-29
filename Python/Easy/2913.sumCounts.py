# 2913. Subarrays Distinct Element Sum of Squares I
# Beats: 58.62%
def sumCounts(nums):
    output =0
    subsets = []
    for i in range(len(nums)):
        for j in range(i+1, len(nums)+1):
            output += (len(set(nums[i:j]))**2)
    return output


nums = [1,2,1]
nums = [1,1]
print(sumCounts(nums))
