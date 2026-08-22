# 3550. Smallest Index With Digit Sum Equal to Index
# Beats: 11.00%
def smallestIndex(nums):
    output = []
    for i in range(len(nums)):
        nums[i] = str(nums[i])
        sum = 0
        for j in range(len(nums[i])):
            sum += int(nums[i][j])
        if i == sum:
            output.append(i)
    if output:
        return min(output)
    else:
        return -1

# nums = [1,10,11]
nums = [1,2,3]
print(smallestIndex(nums))
