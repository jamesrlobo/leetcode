# 2932. Maximum Strong Pair XOR I
# Beats: 19.45%
def maximumStrongPairXor(nums):
    output = []
    for i in range(len(nums)):
        for j in range(len(nums)):
            if abs(nums[i]-nums[j]) <= min(nums[i], nums[j]):
                output.append(nums[i] ^ nums[j])
    return max(output)


nums = [1,2,3,4,5]
nums = [10,100]
nums = [5,6,25,30]
print(maximumStrongPairXor(nums))
