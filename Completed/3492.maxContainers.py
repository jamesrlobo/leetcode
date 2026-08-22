# 3492. Maximum Containers on a Ship
# Beats: 19.07%
def maxContainers(n,w,maxWeight):
    return int(min(n * n, maxWeight / w))


# n = 2
# w = 3
# maxWeight = 15

n = 3
w = 5
maxWeight = 20
print(maxContainers(n, w, maxWeight))
