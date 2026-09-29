#2078. Two Furthest Houses With Different Colors
#Beats: 12.86%
def maxDistance(colors):
    result = 0
    for i in range(len(colors)):
        for j in range(len(colors)):
            if colors[i] != colors[j]:
                distance = abs(i-j)
                if result < distance:
                    result = distance
    return result


# colors = [1,1,1,6,1,1,1]
# colors = [1,8,3,8,3]
colors = [0,1]
print(maxDistance(colors))
