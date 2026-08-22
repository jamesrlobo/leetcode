# 4020. Elevator Requests I
# https://leetcode.com/problems/elevator-requests-i/description/
# Beats: 100.00%
def elevatorRequests(n, requests):
    current_floor = 0
    time = 0
    i = 0
    while i < len(requests):
        # print(requests[i])
        if requests[i] != current_floor:
            time += (abs(current_floor-requests[i]))
            current_floor = requests[i]
        i+=1
    return "Time:", time


n = 5
requests = [2,1,4,3]
n = 3
requests = [2,0,0]
n = 2
requests = [0,1]
print(elevatorRequests(n, requests))
