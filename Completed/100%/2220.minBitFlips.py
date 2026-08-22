# 2220. Minimum Bit Flips to Convert Number
def minBitFlips(start, goal):
    start = list(bin(start)[2:])
    goal = list(bin(goal)[2:])
    print(start, len(start))
    print(goal, len(goal))
    if len(start) != len(goal):
        l = abs(len(start)-len(goal))
        if len(start) < len(goal):
            for i in range(l):
                start.insert(0, '0')
        else:
            for i in range(l):
                goal.insert(0, '0')
    print(start)
    print(goal)
    count, i = 0, 0
    while i< len(goal):
        if start[i] != goal[i]:
            goal[i] = start[i]
            count +=1
        i+=1
    return count

start = 99
goal = 29
# start = 10
# goal = 7
# start = 3
# goal = 4
# start = 81
# goal = 87
print(minBitFlips(start, goal))
