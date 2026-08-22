# 1475. Final Prices With a Special Discount in a Shop
def finalPrices(prices):
    output = []
    for i in range(len(prices)-1):
        print("Main:",prices[i])
        for j in range(i+1, len(prices)):
            print(prices[j])
            if j > i and prices[j] <= prices[i]:
                output.append(prices[i]-prices[j])
                break
        else:
            output.append(prices[i])
    output.append(prices[-1])
    return output

# prices = [8,4,6,2,3]
# prices = [1,2,3,4,5]
# prices = [10,1,1,6]
prices = [8,4,6,2,3]
print(finalPrices(prices))
