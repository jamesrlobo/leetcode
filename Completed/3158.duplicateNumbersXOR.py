# 3158. Find the XOR of Numbers Which Appear Twice
def duplicateNumbersXOR(nums):
    output = 0
    for i in set(nums):
        if nums.count(i) >= 2:
            output ^= i
    return output


nums = [1,2,2,1]
# nums = [1,2,3]
# nums = [1,2,1,3]
print(duplicateNumbersXOR(nums))
