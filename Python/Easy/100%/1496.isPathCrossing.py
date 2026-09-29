# 1496. Path Crossing
# Beats: 100.00%
def isPathCrossing(path):
    northSouth, westEast = 0, 0
    paths = []
    paths.append([northSouth, westEast])
    for i in range(len(path)):
        if path[i] == "N":
            northSouth += 1
        elif path[i] == "S":
            northSouth -= 1
        elif path[i] == "W":
            westEast += 1
        elif path[i] == "E":
            westEast -= 1
        if [northSouth, westEast] not in paths:
            paths.append([northSouth, westEast])
        else:
            return True
    return False

path = "NES"
path = "NESWW"
print(isPathCrossing(path))
