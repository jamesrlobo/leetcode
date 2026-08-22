# 2079. Watering Plants
# Beats: 5.30%
def wateringPlants(plants, capacity):
    steps = 0
    can = capacity
    while set(plants) != {0}:
        for i in range(len(plants)):
            steps += 1
            if plants[i] == 0:
                continue
            elif plants[i] <= can:
                can -= plants[i]
                plants[i] = 0
            else:
                steps += (i-1)
                can = capacity
                break
    return steps


plants = [2,2,3,3]
capacity = 5

plants = [1,1,1,4,2,3]
capacity = 4

plants = [7,7,7,7,7,7,7]
capacity = 8
print(wateringPlants(plants, capacity))
