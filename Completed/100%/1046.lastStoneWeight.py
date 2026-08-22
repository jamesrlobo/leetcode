# 1046. Last Stone Weight
# Beats: 100.00%
def lastStoneWeight(stones):
    if len(stones) == 1:
        return sum(stones)
    while len(stones) > 1:
        stones = sorted(stones, reverse=False)
        print(stones)
        m1 = stones.pop()
        m2 = stones.pop()
        m3 = abs(m1 - m2)
        stones.append(m3)
    return stones


stones = [2,7,4,1,8,1]
# stones = [1]
print(lastStoneWeight(stones))


# def lastStoneWeight(stones):
#     if len(stones) == 1:
#         return sum(stones)
#     while len(stones) > 1:
#         max1 = max(stones)
#         stones.pop(stones.index(max1))
#         max2 = max(stones)
#         stones.pop(stones.index(max2))
#         stones.append(max1 - max2)
#     return sum(stones)
