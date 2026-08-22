# 1800. Maximum Ascending Subarray Sum
def maxAscendingSum(nums):
    if len(nums) == 1:
        return max(nums)
    output = []
    sum = 0
    i = 1
    while i < len(nums):
        if nums[i-1] < nums[i]:
            sum += nums[i-1]
            # print(sum, output)
        else:
            sum += nums[i-1]
            output.append(sum)
            # print(sum, output)
            sum =0
        i+=1
    if nums[-1] < nums[-2]:
        output.append(sum)
        output.append(nums[-1])
    else:
        sum+= nums[-1]
        output.append(sum)
    return max(output)


# nums = [10,20,30,5,10,50]
# nums = [10,20,30,40,50]
# nums = [12,17,15,13,10,11,12]
nums = [6]
print(maxAscendingSum(nums))
