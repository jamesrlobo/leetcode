# 657. Robot Return to Origin
def judgeCircle(moves):
    vertical, horizontal = 0, 0
    moves = list(moves)
    for i in moves:
        if i == "U":
            vertical += 1
        elif i == "D":
            vertical -= 1
        elif i == "R":
            horizontal += 1
        else:
            horizontal -= 1
    if vertical == 0 and horizontal == 0:
        return True
    return False


moves = "LL"
print(judgeCircle(moves))
