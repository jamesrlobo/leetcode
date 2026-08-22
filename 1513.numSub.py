import itertools


def numSub(s):
    count = 0
    subsrtings = [''.join(s[i:j]) for i, j in itertools.combinations(range(len(s)+1), 2)]
    for i in subsrtings:
        if set(i) == {'1'}:
            count += 1
    return count


s = "0110111"
print(numSub(s))
