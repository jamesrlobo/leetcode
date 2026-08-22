# 3312. Sorted GCD Pair Queries
# https://leetcode.com/problems/sorted-gcd-pair-queries/description
import math


def gcdValues(nums, queries):
    gcdPairs = []
    n = len(nums)
    for i in range(n):
        for j in range(i, n):
            if i < j:
                gcdPairs.append(math.gcd(nums[i], nums[j]))
    gcdPairs.sort()
    answer = []
    for i in range(len(queries)):
        answer.append(gcdPairs[queries[i]])
    return answer


nums = [2,3,4]
queries = [0,2,2]

nums = [4,4,2,1]
queries = [5,3,1,0]

nums = [2,2]
queries = [0,0]
print(gcdValues(nums, queries))
