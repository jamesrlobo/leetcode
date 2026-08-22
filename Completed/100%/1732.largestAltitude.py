# 1732. Find the Highest Altitude
# https://leetcode.com/problems/find-the-highest-altitude/description/
# Beats: 100.00%
def largestAltitude(gain):
    altitude = [0]
    curr = 0
    for i in gain:
        altitude.append(curr + i)
        curr = altitude[-1]
    return max(altitude)


gain = [-5,1,5,0,-7]
gain = [-4,-3,-2,-1,4,3,2]
print(largestAltitude(gain))
