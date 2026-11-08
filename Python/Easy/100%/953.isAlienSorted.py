# 953. Verifying an Alien Dictionary
# https://leetcode.com/problems/verifying-an-alien-dictionary/?envType=problem-list-v2&envId=array
# Beats: 100.00%
def isAlienSorted(self, words: list[str], order: str) -> bool:
    for j in range(1, len(words)):
        first = words[j-1]
        second = words[j]
        if first == second:
            continue
        length = min(len(first), len(second))
        if second == first[:length]:
            return False
        for x, y in zip(first, second):
            if x != y:
                if order.index(x) > order.index(y):
                    return False
                else:
                    break
    return True
