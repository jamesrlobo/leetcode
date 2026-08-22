# 3842. Toggle Light Bulbs
# Beats: 5.93%
def toggleLightBulbs(bulbs):
    output = [x for x in set(bulbs) if bulbs.count(x)%2 != 0]
    return sorted(output)


bulbs = [10,30,20,10]
bulbs = [100,100]
print(toggleLightBulbs(bulbs))
