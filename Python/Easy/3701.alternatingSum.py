# 3701. Compute Alternating Sum
def alternatingSum(nums):)
    output, i = 0, 0
    while i < len(nums):
        if i%2 == 0:
            output += nums[i]
        else:
            output -= nums[i]
        i+=1
    return output


# nums = [1,3,5,7]
nums = [100]
print(alternatingSum(nums))
