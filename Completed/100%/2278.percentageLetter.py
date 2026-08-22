# 2278. Percentage of Letter in String
# https://leetcode.com/problems/percentage-of-letter-in-string/description/
# Beats: 100.00%
def percentageLetter(s, letter):
    occurrences = s.count(letter)
    n = len(s)
    return int((occurrences / n) * 100)


s = "foobar"
letter = "o"

s = "jjjj"
letter = "k"
print(percentageLetter(s, letter))
