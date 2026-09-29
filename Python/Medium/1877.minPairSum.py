# 1877. Minimize Maximum Pair Sum in Array
# Beats: 86.00%
def minPairSum(nums):
    output = []
    nums = sorted(nums)
    mid = len(nums)//2
    firstHalf = nums[:mid]
    secondHalf = nums[mid:]
    for i, j in zip(firstHalf, secondHalf[::-1]):
        output.append(i + j)
    return max(output)

nums = [3,5,2,3]
nums = [3,5,4,2,4,6]
print(minPairSum(nums))
