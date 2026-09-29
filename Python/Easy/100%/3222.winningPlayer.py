# 3222. Find the Winning Player in Coin Game
# https://leetcode.com/problems/find-the-winning-player-in-coin-game/description/
# Beats: 100.00%
def winningPlayer(x, y):
    turn =  int(min(x,y/4))
    if turn%2 == 0:
        return "Bob"
    return "Alice"


x = 2
y = 7
# x = 4
# y = 11
print(winningPlayer(x, y))
