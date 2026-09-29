# 3769. Sort Integers by Binary Reflection
# Beats: 100.00%
def sortByReflection(nums):
    output = []
    for i in range(len(nums)):
        nums[i] = [nums[i], int(bin(nums[i])[2:][::-1], 2)]
    nums = sorted(nums, key=lambda x:x[0])
    nums = sorted(nums, key=lambda x: x[1])
    for j in nums:
        output.append(j[0])
    return output


# nums = [4,5,4]
# nums = [3,6,5,8]
nums = [8,2]
print(sortByReflection(nums))
