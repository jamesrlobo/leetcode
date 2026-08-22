# 2391. Minimum Amount of Time to Collect Garbage
# Beats: 40.00%
def garbageCollection(garbage, travel):
    types = ["P", "G", "M"]
    travel.insert(0, 0)
    finalOutput = []
    for type in types:
        output, temp = 0, 0
        for i in range(len(garbage)):
            if type not in garbage[i]:
                temp += travel[i]
                continue
            else:
                output += travel[i] + temp
                temp = 0
                output += garbage[i].count(type)
        finalOutput.append(output)
    return sum(finalOutput)


garbage = ["G","P","GP","GG"]
travel = [2,4,3]

garbage = ["MMM","PGM","GP"]
travel = [3,10]
print(garbageCollection(garbage, travel))
