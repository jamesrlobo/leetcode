# 1833. Maximum Ice Cream Bars
# Beats: 74.96%
def maxIceCream(costs, coins):
    count = 0
    costs = sorted(costs)
    for i in costs:
        if i <= coins:
            count += 1
            coins -= i
        else:
            return count
    return count


# costs = [1,3,2,4,1]
# coins = 7
# costs = [10,6,8,7,7,8]
# coins = 5
costs = [1,6,3,1,2,5]
coins = 20
print(maxIceCream(costs, coins))
