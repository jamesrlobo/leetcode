# 3309. Maximum Possible Number by Binary Concatenation
# Beats:100.00%
def maxGoodNumber(nums):
    output = []
    combo1 = nums
    combo2 = [nums[0], nums[2], nums[1]]
    combo3 = [nums[1], nums[2], nums[0]]
    combo4 = [nums[1], nums[0], nums[2]]
    combo5 = [nums[2], nums[0], nums[1]]
    combo6 = [nums[2], nums[1], nums[0]]
    combos = [combo1, combo2, combo3, combo4, combo5, combo6]
    for i in combos:
        temp = ""
        for j in i:
            temp +=(bin(j)[2:])
        output.append(int(temp, 2))
    return max(output)


nums = [1,2,3]
nums = [2,8,16]
nums = [1,18,27]
print(maxGoodNumber(nums))
