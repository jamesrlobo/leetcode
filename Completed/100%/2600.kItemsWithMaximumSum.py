# 2600. K Items With the Maximum Sum
# https://leetcode.com/problems/k-items-with-the-maximum-sum/
# Beats: 100.00%
def kItemsWithMaximumSum(numOnes, numZeros, numNegOnes, k):
    bag = []
    for x in range(numOnes):
        bag.append(1)
    for y in range(numZeros):
        bag.append(0)
    for z in range(numNegOnes):
        bag.append(-1)
    return sum(bag[:k])


numOnes = 3
numZeros = 2
numNegOnes = 0
k = 2

numOnes = 3
numZeros = 2
numNegOnes = 0
k = 4

numOnes = 6
numZeros = 6
numNegOnes = 6
k = 13

numOnes = 4
numZeros = 0
numNegOnes = 1
k = 2
print(kItemsWithMaximumSum(numOnes, numZeros, numNegOnes, k))
