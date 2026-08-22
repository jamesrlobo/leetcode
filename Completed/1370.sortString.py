# 1370. Increasing Decreasing String
# Beats: 5.39%
def sortString(s):
    output = []
    s = list(s)
    turn = 0
    while len(s) > 0:
        if turn%2 == 0:
            temp = []
            unique = list(set(s))
            for i in range(len(unique)):
                if (min(unique)) not in temp:
                    temp.append(min(unique))
                    # print(unique)
                    s.remove(min(unique))
                    unique.remove(min(unique))
            turn += 1
            output += temp
        else:
            temp = []
            unique = list(set(s))
            for i in range(len(unique)):
                if (max(unique)) not in temp:
                    temp.append(max(unique))
                    # print(unique)
                    s.remove(max(unique))
                    unique.remove(max(unique))
            turn += 1
            output += temp
    return "".join(output)


# s = "aaaabbbbcccc"
s = "rat"
print(sortString(s))
