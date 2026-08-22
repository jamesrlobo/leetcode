# 3560. Find Minimum Log Transportation Cost
# Beats: 100.00%
def minCuttingCost(n, m, k):
    cost = 0
    if n <= k and m <= k:
        return cost
    if n > k and m > k:
        cost = (k*(n-k)) + (k*(m-k))
    elif n > k or m > k:
        cost = (k * (max(m, n) - k))
    return cost


n = 6
m = 5
k = 5
print(minCuttingCost(n, m, k))
