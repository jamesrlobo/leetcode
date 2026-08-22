# 441. Arranging Coins
# Beats: 34.94%
def arrangeCoins(n):
    i = 0
    while i < n:
        i += 1
        n -= i
    return i


    return step


n = 5
print(arrangeCoins(n))
