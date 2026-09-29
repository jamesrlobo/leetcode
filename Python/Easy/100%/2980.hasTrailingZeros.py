# 2980. Check if Bitwise OR Has Trailing Zeros
# Beats: 100.00%
def hasTrailingZeros(nums):
    even = 0
    for i in nums:
        if i%2 == 0:
            even += 1
        if even == 2:
            return True
    return False


nums = [1,2,3,4,5]
nums = [2,4,8,16]
nums = [1,3,5,7,9]
print(hasTrailingZeros(nums))


# def hasTrailingZeros(nums):
#     for i in range(len(nums)):
#         for j in range(len(nums)):
#             if i != j:
#                 if (int(bin(nums[i] | nums[j])[2:])%10) == 0:
#                     return True
#     return False
