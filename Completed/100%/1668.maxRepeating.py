# 1668. Maximum Repeating Substring
# https://leetcode.com/problems/maximum-repeating-substring/description/
#Beats: 100.00%
def maxRepeating(sequence,word):
    count = 0
    repeated = word
    while repeated in sequence:
        count+=1
        repeated += word
    return count


sequence = "aaabaaaabaaabaaaabaaaabaaaabaaaaba"
word = "aaaba"
# sequence = "ababc"
# word = "ab"
# sequence = "ababc"
# word = "ba"
# sequence = "ababc"
# word = "ac"
print(maxRepeating(sequence, word))
