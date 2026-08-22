# 3467. Transform Array by Parity
def transformArray(nums):
    output = []
    for i in nums:
        if i%2 == 0:
            output.append(0)
        else:
            output.append(1)
    output.sort()
    return output

# nums = [4,3,2,1]
nums = [1,5,1,4,2]
print(transformArray(nums))
