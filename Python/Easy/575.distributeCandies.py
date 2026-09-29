# 575. Distribute Candies
# Beats: 76.95%
def distributeCandies(candyType):
    canEat = int(len(candyType)/2)
    diffTypeCandies = len(set(candyType))
    return min(canEat, diffTypeCandies)


candyType = [1,1,2,2,3,3]
# candyType = [1,1,2,3]
# candyType = [6,6,6,6]
print(distributeCandies(candyType))
