# 3248. Snake in Matrix
# Beats: 47.47%
def finalPositionOfSnake(n, commands):
    grid = []
    for i in range(n*n):
        grid.append(i)
    position = 0
    for j in range(len(commands)):
        if commands[j] == "RIGHT":
            position +=1
        elif commands[j] == "LEFT":
            position -= 1
        elif commands[j] == "DOWN":
            position += n
        elif commands[j] == "UP":
            position -= n
    return position


# n = 2
# commands = ["RIGHT","DOWN"]
n = 3
commands = ["DOWN","RIGHT","UP"]
print(finalPositionOfSnake(n, commands))
