# 2410. Maximum Matching of Players With Trainers
# https://leetcode.com/problems/maximum-matching-of-players-with-trainers/description/
# Beats: 8.06%
def matchPlayersAndTrainers(self, players: list[int], trainers: list[int]) -> int:
    players = sorted(players)
    trainers = sorted(trainers)
    count = 0
    i, j = 0, 0
    while i < len(players) and j < len(trainers):
        if players[i] <= trainers[j]:
            count += 1
            i+= 1
        j+=1
    return count
