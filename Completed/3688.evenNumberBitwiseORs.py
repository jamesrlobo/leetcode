# 3688. Bitwise OR of Even Numbers in an Array
def evenNumberBitwiseORs(nums):
    output = 0
    for i in nums:
        if i%2 == 0:
            output = output | i
    return output


# nums = [1,2,3,4,5,6]
# nums = [7,9,11]
nums = [1,8,16]
print(evenNumberBitwiseORs(nums))
