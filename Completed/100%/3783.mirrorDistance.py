# 3783. Mirror Distance of an Integer
# Beats: 100.00%
def mirrorDistance(n):
    return abs(n - int(str(n)[::-1]))


n = 25
n = 10
n = 7
print(mirrorDistance(n))
