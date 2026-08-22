# 1404. Number of Steps to Reduce a Number in Binary Representation to One
# Beats: 100.00%
def numSteps(s):
    count = 0
    s = int(s, 2)
    while s != 1:
        if s%2 == 0:
            s = s//2
        else:
            s += 1
        count += 1
    return count


s = "1101"
s = "10"
s = "1"
print(numSteps(s))
