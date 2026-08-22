# 3206. Alternating Groups I
# Beats: 45.89%
def numberOfAlternatingGroups(colors):
    output = 0
    for i in range(len(colors)-1):
        # print(colors[i-1], colors[i], colors[i+1])
        if colors[i-1] != colors[i] and colors[i] != colors[i+1]:
            output += 1
    # print(colors[i], colors[i+1], colors[0])
    if colors[i] != colors[i+1] and colors[i+1] != colors[0]:
        output += 1
    return output


# colors = [1,1,1]
# colors = [0,1,0,0,1]
print(numberOfAlternatingGroups(colors))
