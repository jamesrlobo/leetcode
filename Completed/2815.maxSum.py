# 2815. Max Pair Sum in an Array
# Beats: 50.72%
def maxSum(nums):
    output = []
    nums = sorted(nums, reverse=True)
    d = {}
    for num in nums:
        if max(str(num)) not in d:
            d[max(str(num))] = [num]
        else:
            d[max(str(num))] += [num]
    for item in d:
        if len(d[item]) > 1:
            temp = d[item]
            output.append(temp[0]+temp[1])
    if len(output) > 0:
        return max(output)
    return -1


nums = [112,131,411]
nums = [2536,1613,3366,162]
nums = [51,71,17,24,42]
print(maxSum(nums))
