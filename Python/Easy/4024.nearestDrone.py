# 4024. Nearest Available Drone
# https://leetcode.com/problems/nearest-available-drone/description/
# Beats: 9.27%
def nearestDrone(drones, target):
    d = {}
    for drone in drones:
        range = (abs(drone[0]-target[0])+abs(drone[1]-target[1]))
        if range <= drone[2]:
            # print(range, drones.index(drone))
            if range not in d:
                d[range] = [drones.index(drone)]
            else:
                d[range] += [drones.index(drone)]
    # print(d)
    if d:
        return min(d[min(d)])
    return -1


# drones = [[0,0,8],[2,2,9]]
# target = [3,4]
# drones = [[2,1,5],[4,4,5],[6,6,8]]
# target = [5,5]
drones = [[4,4,5]]
target = [8,6]
print(nearestDrone(drones, target))
