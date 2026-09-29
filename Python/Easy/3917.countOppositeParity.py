# 3917. Count Indices With Opposite Parity
# https://leetcode.com/problems/count-indices-with-opposite-parity/description/
# Beats: -%
def countOppositeParity(nums):
    n = len(nums)
    for i in range(n):
        # print(nums[i])
        # print("-------------")
        parityIndex = 0
        if nums[i]%2 != 0:
            for j in range(i+1, n):
                if nums[j]%2 == 0:
                    # print(j)
                    parityIndex += 1
        else:
            for j in range(i+1, n):
                if nums[j]%2 != 0:
                    # print(j)
                    parityIndex += 1
        # print(parityIndex)
        nums[i] = parityIndex
        # print("---------------")
    return nums


nums = [1,2,3,4]
# nums = [1]
# nums = [4,1]
print(countOppositeParity(nums))
