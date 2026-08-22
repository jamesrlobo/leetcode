# 461. Hamming Distance
# Beats: 100.00%
def hammingDistance(x, y):
    count = 0
    x = bin(x)[2:]
    y = bin(y)[2:]
    if len(x) >= len(y):
        maximum = len(x)
    else:
        maximum = len(y)
    x = x.zfill(maximum)
    y = y.zfill(maximum)
    for i,j in zip(x,y):
        if i != j:
            count += 1
    return count


x = 680142203
y = 1111953568

print(hammingDistance(x,y))
