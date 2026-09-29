# 3178. Find the Child Who Has the Ball After K Seconds
# Beats: 100.00%
def numberOfChild(n, k):
    direction = True
    current = 0
    pos = 0
    while current != k:
        if direction == True:
            current += 1
            pos += 1
        else:
            current += 1
            pos -= 1
        if pos == (n-1):
            direction = False
        if pos == 0:
            direction = True
        # print(current, pos)
    return pos


n = 3
k = 5

n = 5
k = 6

n = 4
k = 2
print(numberOfChild(n, k))
