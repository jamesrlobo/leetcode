# 4111. Count Consistent Subarrays I
# https://leetcode.com/problems/count-consistent-subarrays-i/
# Beats: 6.60%
def countConsistent(nums):
    n = len(nums)
    output = 0
    subarrays = []
    for i in range(n):
        for j in range(i, n+1):
            if len(nums[i:j]) == 0:
                output += 1
            elif len(nums[i:j]) > 1:
                subarrays.append(nums[i:j])
    for subarray in subarrays:
        minVal = min(subarray)
        result = subarray[0]
        for num in subarray[1:]:
            result &= num
            if result == 0:
                break
        if minVal == result:
            output += 1
    return output


nums = [5,3,1,2]
print(countConsistent(nums))
