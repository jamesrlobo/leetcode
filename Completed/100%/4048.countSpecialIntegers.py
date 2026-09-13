# 4048. Count Values With Equally Spaced Occurrences I
# https://leetcode.com/problems/count-values-with-equally-spaced-occurrences-i/description/
# Beats: 100.00%
def countSpecialIntegers(nums):
    output = 0
    for i in set(nums):
        if nums.count(i) == 3:
            indices = []
            for j in range(len(nums)):
                if nums[j] == i:
                    indices.append(j)
                if len(indices) == 3:
                    break
            if indices[1] - indices[0] == indices[2]- indices[1]:
                output += 1
    return output


nums = [1,8,1,5,1,5,8,5]
nums = [8,8,8,8]
nums = [8,6,6,8,8]
print(countSpecialIntegers(nums))
