# 1518. Water Bottles
# Beats: 100.00%
def numWaterBottles(numBottles, numExchange):
    count = numBottles
    numEmptyBottles = numBottles
    while numEmptyBottles >= numExchange:
        # print("numEmptyBottles:", numEmptyBottles)
        numBottles = numEmptyBottles//numExchange
        numEmptyBottles = numEmptyBottles%numExchange
        # print("Full bottles after excahnge:", numBottles)
        # print("Remaining Empty bottles:", numEmptyBottles)
        count += numBottles
        numEmptyBottles += numBottles
        numBottles = 0
    return count



numBottles = 9
numExchange = 3

# numBottles = 15
# numExchange = 4
print(numWaterBottles(numBottles, numExchange))
