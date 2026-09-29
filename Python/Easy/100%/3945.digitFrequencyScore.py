# 3945. Digit Frequency Score
# https://leetcode.com/problems/digit-frequency-score/description/
# Beats: 100.00%
def digitFrequencyScore(n):
    n = str(n)
    output = 0
    for i in set(n):
        output += int(i) * n.count(i)
    return output


n = 122
n = 101
print(digitFrequencyScore(n))


# output = 0
# for i in str(n):
#     output += int(i)
# return output
