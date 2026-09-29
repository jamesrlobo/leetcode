# 2176. Count Equal and Divisible Pairs in an Array
def countPairs(nums):
    output = 0
    for i in range(len(nums)):
        for j in range(len(nums)):
            print(i,j)
            if i < j < len(nums):
                if nums[i] == nums[j] and (i*j)%k == 0:
                    output +=1
    return output


# nums = [1,2,3,4]
# k = 1
# nums = [3,1,2,2,2,1,3]
# k = 2
nums = [5,5,9,2,5,5,9,2,2,5,5,6,2,2,5,2,5,4,3]
k = 7
print(countPairs(nums))
