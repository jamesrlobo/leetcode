# 2558. Take Gifts From the Richest Pile
# Beats: 6.55%
import math

def pickGifts(gifts,k):
    i = 0
    while i < k:
        maximum = max(gifts)
        maximum_index = gifts.index(max(gifts))
        gifts[maximum_index] = int(math.sqrt(maximum))
        i +=1
    return sum(gifts)


# gifts = [25,64,9,4,100]
# k = 4
gifts = [1,1,1,1]
k = 4
print(pickGifts(gifts,k))
