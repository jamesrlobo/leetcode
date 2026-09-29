# 1523. Count Odd Numbers in an Interval Range
def countOdds(low, high):
    n = (high - low + 1)
    print(n)
    if n%2 == 0:
        return int(n/2)
    else:
        if low%2 != 0 or high%2 !=0:
            return int(n/2 +1)
        else:
            return int(n/2)


# low = 3
# high = 7
low = 8
high = 10
# low = 798273637
# high = 970699661
# low = 0
# high = 10
print(countOdds(low, high))
