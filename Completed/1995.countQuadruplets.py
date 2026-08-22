# 1995. Count Special Quadruplets
# Beats: 8.25%
def countQuadruplets(nums):
    length = len(nums)
    output = 0
    for i in range(length):
        for j in range(i+1, length):
            for k in range(j+1, length):
                for l in range(k+1, length):
                    if (nums[i] + nums[j] + nums[k]) == nums[l]:
                        print(nums[i], nums[j], nums[k])
                        output +=1
    return output


# nums = [1,2,3,6]
# nums = [3,3,6,4,5]
nums = [1,1,1,3,5]
print(countQuadruplets(nums))
