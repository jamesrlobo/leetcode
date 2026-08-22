# 3477. Fruits Into Baskets II
def numOfUnplacedFruits(fruits, baskets):
    for i in range(len(fruits)):
        print("Fruits:", fruits[i], baskets)
        for j in range(len(baskets)):
            if fruits[i] <= baskets[j]:
                baskets.pop(j)
                break
    return len(baskets)


fruits = [4,2,5]
baskets = [3,5,4]
# fruits = [3,6,1]
# baskets = [6,4,7]
# fruits = [8,5]
# baskets = [1,8]
print(numOfUnplacedFruits(fruits, baskets))
