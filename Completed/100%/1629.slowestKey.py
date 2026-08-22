# 1629. Slowest Key
# https://leetcode.com/problems/slowest-key/description/
# Beats: 100.00%
def slowestKey(releaseTimes, keysPressed):
    releaseTimes.insert(0, 0)
    # print(releaseTimes)
    d = {}
    for i in range(1, len(releaseTimes)):
        temp = (releaseTimes[i] - releaseTimes[i-1] )
        if temp not in d:
            d[temp] = [i]
        else:
            d[temp] += [i]
    print(d)
    maximum_keypress = max(d)
    print(maximum_keypress)
    output = []
    for ch in d[maximum_keypress]:
        output.append(keysPressed[ch-1])
    return max(output)


releaseTimes = [9,29,49,50]
keysPressed = "cbcd"
releaseTimes = [12,23,36,46,62]
keysPressed = "spuda"
releaseTimes = [23,34,43,59,62,80,83,92,97]
keysPressed = "qgkzzihfc"
releaseTimes = [1,2]
keysPressed = "ba"
print(slowestKey(releaseTimes, keysPressed))
