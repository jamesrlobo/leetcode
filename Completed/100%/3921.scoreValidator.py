# 3921. Score Validator
# https://leetcode.com/problems/score-validator/description/
# Beats: 100.00%
def scoreValidator(events):
    n = len(events)
    score, counter = 0, 0
    for i in range(n):
        if events[i] in ["0", "1", "2", "3", "4", "6"]:
            score += int(events[i])
        elif events[i] == "W":
            counter += 1
        elif events[i] == "WD":
            score += 1
        elif events[i] == "NB":
            score += 1
        if counter == 10:
            break
    return [score, counter]


events = ["1","4","W","6","WD"]
events = ["WD","NB","0","4","4"]
events = ["W","W","W","W","W","W","W","W","W","W","W"]
print(scoreValidator(events))
