# 1710. Maximum Units on a Truck
def maximumUnits(boxTypes, truckSize):
    boxTypes = sorted(boxTypes, key=lambda x: x[1], reverse=True)
    print(boxTypes)
    count = 0
    units = 0
    for i in range(len(boxTypes)):
        for j in range(boxTypes[i][0]):
            if (count+1) <= truckSize:
                count += 1
                units += boxTypes[i][1]
            else:
                return units
    return units


# boxTypes = [[1,3],[5,5],[2,5],[4,2],[4,1],[3,1],[2,2],[1,3],[2,5],[3,2]]
# truckSize = 35
# boxTypes = [[1,3],[5,5],[2,5],[4,2],[4,1],[3,1],[2,2],[1,3],[2,5],[3,2]]
# truckSize = 35
boxTypes = [[1,3],[2,2],[3,1]]
truckSize = 4
# boxTypes = [[5,10],[2,5],[4,7],[3,9]]
# truckSize = 10
print(maximumUnits(boxTypes, truckSize))
