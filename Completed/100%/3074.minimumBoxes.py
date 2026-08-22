# 3074. Apple Redistribution into Boxes
# Beats: 100.00%
def minimumBoxes(apple, capacity):
    capacity = sorted(capacity, reverse=True)
    totalApples = sum(apple)
    i, output = 0, 0
    while totalApples > 0:
        totalApples -= capacity[i]
        output += 1
        i+=1
    return output


apple = [1,3,2]
capacity = [4,3,1,5,2]

apple = [5,5,5]
capacity = [2,4,2,7]
print(minimumBoxes(apple, capacity))
