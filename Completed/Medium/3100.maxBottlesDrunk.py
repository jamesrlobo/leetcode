# 3100. Water Bottles II
# Beats: 68.80%
def maxBottlesDrunk(numBottles, numExchange):
    emptyBottles = numBottles
    drunkBottles = numBottles
    numBottles = 0
    while emptyBottles >= numExchange:
        emptyBottles -= numExchange
        numExchange +=1
        numBottles +=1
        emptyBottles += numBottles
        drunkBottles += numBottles
        numBottles = 0
        print("emptyBottles:", emptyBottles)
        print("drunkBottles:", drunkBottles)
        print("numBottles:", numBottles)
    return drunkBottles


numBottles = 13
numExchange = 6
# numBottles = 10
# numExchange = 3
print(maxBottlesDrunk(numBottles, numExchange))
