# 3427. Sum of Variable Length Subarrays
# Beats: 55.43%
def subarraySum(nums):
    output = 0
    for i in range(len(nums)):
        # print("i:", i)
        start = max(0, i-nums[i])
        # print("Start:", nums[start])
        print(nums[start:i+1])
        output += sum(nums[start:i+1])
    return output


nums = [2,3,1]
nums = [3,1,1,2]
print(subarraySum(nums))
