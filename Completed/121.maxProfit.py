# 121. Best Time to Buy and Sell Stock
def maxProfit(prices):
    profit = 0
    buy = prices[0]
    for sell in prices[1:]:
        if sell > buy:
            profit = max(profit, sell - buy)
        else:
            buy = sell
    return profit

prices = [7,1,5,3,6,4]
# prices = [7,6,4,3,1]
# prices = [2,1,2,0,1]
print(maxProfit(prices))
