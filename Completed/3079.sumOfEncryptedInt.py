# 3079. Find the Sum of Encrypted Integers
def sumOfEncryptedInt(nums):
    result = []
    for i in range(len(nums)):
        output = ""
        # l = len(list(str(nums[i])))
        # m = max(list(str(nums[i])))
        for k in range(len(list(str(nums[i])))):
            output += max(list(str(nums[i])))
        result.append(int(output))
    return sum(result)


# nums = [10,21,31]
nums = [1,2,3]
print(sumOfEncryptedInt(nums))
