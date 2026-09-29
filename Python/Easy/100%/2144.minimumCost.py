# 2144. Minimum Cost of Buying Candies With Discount
# Beats: 100.00%
def minimumCost(cost):
    output = 0
    cost = sorted(cost, reverse=True)
    while len(cost) >= 3:
        output += sum(cost[0:0+2])
        cost.pop(2)
        cost.pop(1)
        cost.pop(0)
    if len(cost) <=2:
        output += sum(cost)
    return output


# cost = [6,5,7,9,2,2]
# cost = [1,2,3]
cost = [5,5]
print(minimumCost(cost))
