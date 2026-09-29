# 2149. Rearrange Array Elements by Sign
# Beats: 71.19%
def rearrangeArray(nums):
    output, pos, neg = [], [], []
    for i in nums:
        if i > 0:
            pos.append(i)
        else:
            neg.append(i)
    for x, y in zip(pos, neg):
        output.append(x)
        output.append(y)
    return output


nums = [3,1,-2,-5,2,-4]
print(rearrangeArray(nums))
