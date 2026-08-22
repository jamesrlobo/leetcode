# 3227. Vowels Game in a String
# Beats: 51.30%
def doesAliceWin(s):
    vowels = "aeiou"
    totalVowels = []
    for i in range(len(s)):
        if s[i] in vowels:
            totalVowels.append(i)
    print(totalVowels)
    # If there are no vowels in the initial string, then Bob wins.
    n = len(totalVowels)
    if n <= 0:
        return False
    # If the number of vowels in the initial string is odd, then Alice can remove the whole string on her first turn and win.
    if n%2 != 0:
        return True
    # What if the number of vowels in the initial string is even? What’s the optimal play for Alice’s first turn?
    return


s =  "leetcoder"
print(doesAliceWin(s))
