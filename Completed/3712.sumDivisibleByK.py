# 3712. Sum of Elements With Frequency Divisible by K
# Beats: 49.18%
def sumDivisibleByK(nums,k):
    output = []
    for i in set(nums):
        if nums.count(i)%k == 0:
            output.append(i*nums.count(i))
    return sum(output)


# nums = [1,2,2,3,3,3,3,4]
# k = 2
# nums = [1,2,3,4,5]
# k = 2
nums = [4,4,4,1,2,3]
k = 3
print(sumDivisibleByK(nums,k))
