# 3516. Find Closest Person
def findClosest(x, y, z):
    if abs(z-x) == abs(z-y):
        return 0
    elif abs(z-x) > abs(z-y):
        return 2
    else:
        return 1


# x, y, z = 2, 7, 4
# x, y, z = 2, 5, 6
x, y, z = 1, 5, 3
print(findClosest(x, y, z))
