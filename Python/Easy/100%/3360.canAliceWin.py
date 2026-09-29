# 3360. Stone Removal Game
# Beats: 100.00%
def canAliceWin(n):
    val = 10
    turn = 0
    while n >= val:
        n = n - val
        val = val-1
        turn +=1
        print(f'N: {n} | Value: {val} | Turn: {turn}')
    if turn%2 != 0:
        return True
    else:
        return False


n = 19
# n = 1
print(canAliceWin(n))
