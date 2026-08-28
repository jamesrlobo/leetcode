# 1823. Find the Winner of the Circular Game
# https://leetcode.com/problems/find-the-winner-of-the-circular-game/
# Beats: 42.29% (Copied from solutions)
def findTheWinner(n, k):
    friends = [x for x in range(1, n+1)]
    print(friends)
    start = 0
    while len(friends) > 1:
        temp = (start + k -1)%len(friends)
        friends.pop(temp)
        start = temp
    return friends[0]


n = 5
k = 2

n = 6
k = 5

n = 3
k = 1

n = 5
k = 4
print(findTheWinner(n, k))
