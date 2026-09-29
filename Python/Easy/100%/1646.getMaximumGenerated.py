# 1646. Get Maximum in Generated Array
# https://leetcode.com/problems/get-maximum-in-generated-array/description/
# Beats: 100.00%
def getMaximumGenerated(n):
    result = []
    for i in range(n+1):
        if i == 0:
            result.append(0)
        elif i == 1:
            result.append(1)
        elif i%2 == 0:
            result.append(result[i//2])
        else:
            result.append(result[(i-1)//2] + result[(i-1)//2 + 1])
    return max(result)


n = 7
print(getMaximumGenerated(n))
