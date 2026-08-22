1925. Count Square Sum Triples
Beats: 80.06%
import math


def countTriples(n):
    output = 0
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            s = math.sqrt((i*i)+(j*j))
            if int(s) == s and s <= n:
                output += 2
    return output


n = 10
print(countTriples(n))
