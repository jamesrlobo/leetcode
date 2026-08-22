# 1863. Sum of All Subset XOR Totals
def subsetXORSum(nums):
    output = 0
    n = len(nums)
    res = []
    for i in range(1 << n):
        subset = []
        for j in range(n):
            if i & (1 << j):
                subset.append(nums[j])
        res.append(subset)
    res = sorted(res)
    for j in res:
        temp =0
        if len(j) < 2:
            output += sum(j)
        else:
            for k in j:
                temp = temp ^ k
        output += temp
    return output


nums = [1,3]
# nums = [5,1,6]
print(subsetXORSum(nums))
