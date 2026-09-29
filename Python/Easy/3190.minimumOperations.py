# 3190. Find Minimum Operations to Make All Elements Divisible by Three
def minimumOperations(nums):
    output =  0
    for i in nums:
        if i%3 == 1:
            output +=1
        elif i%3 == 2:
            output +=1
    return output


# nums = [1,2,3,4]
nums = [3,6,9]
print(minimumOperations(nums))
