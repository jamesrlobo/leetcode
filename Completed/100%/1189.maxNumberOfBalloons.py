# 1189. Maximum Number of Balloons
# https://leetcode.com/problems/maximum-number-of-balloons/description/
# Beats: 100.00%
def maxNumberOfBalloons(text):
    count1 = text.count('b')
    count2 = text.count('a')
    count3 = text.count('l')
    count4 = text.count('o')
    count5 = text.count('n')
    count6 = count3//2
    count7 = count4//2
    maxcount = min(count1, count2, count6, count7, count5)
    return maxcount


text = "nlaebolko"
text = "loonbalxballpoon"
text = "leetcode"
print(maxNumberOfBalloons(text))
