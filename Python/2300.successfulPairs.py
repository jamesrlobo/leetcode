# https://leetcode.com/problems/successful-pairs-of-spells-and-potions/
# 2300. Successful Pairs of Spells and Potions
def successfulPairs(spells, potions, success):
    output = []
    potions = sorted(potions)
    for i in range(len(spells)):
        count = 0
        for j in range(len(potions)):
            if spells[i]*potions[j] >= success:
                count += len(potions[j:])
                break
        output.append(count)
    return output


spells = [5,1,3]
potions = [1,2,3,4,5]
success = 7

spells = [3,1,2]
potions = [8,5,8]
success = 16
print(successfulPairs(spells, potions, success))
