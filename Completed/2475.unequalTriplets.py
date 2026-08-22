# 2475. Number of Unequal Triplets in Array
# Beats: 48.75%
def unequalTriplets(nums):
    output = 0
    length = len(nums)
    for i in range(length):
        for j in range(i+1, length):
            for k in range(j+1, length):
                if nums[i] != nums[j] and nums[i] != nums[k] and nums[j] != nums[k]:
                    output += 1
    return output


nums = [4,4,2,4,3]
# nums = [1,1,1,1,1]
print(unequalTriplets(nums))
