# 260. Single Number III
# Beats: 7.09%
def singleNumber(nums):
    output = []
    for i in set(nums):
        if nums.count(i) == 1:
            output.append(i)
    return output


nums = [1,2,1,3,2,5]
nums = [-1,0]
nums = [0,1]
print(singleNumber(nums))
