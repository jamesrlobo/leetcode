# 2027. Minimum Moves to Convert String
# Beats: 6.38%
def minimumMoves(s):
    i, count = 0, 0
    if set(s) == {'O'}:
        return 0
    s = list(s)
    print(s)
    while i < len(s)-2:
        if s[i] == 'X':
            print(s[i:i+3] )
            if set(s[i:i+3]) != {'O'} or set(s[i:i+3]) == {'X'}:
                s[i:i+3] = ['O','O','O']
                count += 1
            print(s, count)
        i+=1
    if set(s[i-1:]) != {'O'}:
        s[i-1:] = ['O','O','O']
        count += 1
    return count, s


# s = "XXX"
# s = "XXXOX"
# s = "OOOO"
s = "OXOX"
print(minimumMoves(s))
