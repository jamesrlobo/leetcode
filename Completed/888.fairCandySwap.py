# 888. Fair Candy Swap (Copied from solutions)
# Beats: 16.07%
def fairCandySwap(aliceSizes, bobSizes):
    alsum = sum(aliceSizes)
    bobsum = sum(bobSizes)
    k = (alsum + bobsum)//2

    for i in aliceSizes:
        num = k - (alsum - i)
        if num in bobSizes:
            res = [i, num]
            return res


# aliceSizes = [1,1]
# bobSizes = [2,2]

# aliceSizes = [1,2]
# bobSizes = [2,3]

aliceSizes = [2]
bobSizes = [1,3]
print(fairCandySwap(aliceSizes, bobSizes))
