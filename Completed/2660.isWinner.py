# 2660. Determine the Winner of a Bowling Game
# Beats: 90.36%
def isWinner(player1, player2):
    def calculateScore(player):
        sum = 0
        for i in range(len(player)):
            if i == 0:
                sum += player[i]
            elif i == 1:
                if player[i-1] == 10:
                    sum += (player[i]*2)
                else:
                    sum += (player[i])
            else:
                if player[i-2] == 10 or player[i-1] == 10:
                    sum += (player[i]*2)
                else:
                    sum += (player[i])
        return sum
    sum1 = calculateScore(player1)
    sum2 = calculateScore(player2)
    if sum1 > sum2:
        return 1
    elif sum1 < sum2:
        return 2
    else:
        return 0


player1 = [5,10,3,2]
player2 = [6,5,7,3]

player1 = [3,5,7,6]
player2 = [8,10,10,2]

player1 = [2,3]
player2 = [4,1]

player1 = [1,1,1,10,10,10,10]
player2 = [10,10,10,10,1,1,1]
print(isWinner(player1, player2))
