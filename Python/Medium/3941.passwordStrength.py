# 3941. Password Strength
# https://leetcode.com/problems/password-strength/description/
# Beats: 89.55%
def passwordStrength(password):
    point = 0
    for i in set(password):
        if i in "abcdefghijklmnopqrstuvwxyz":
            point += 1
        elif i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            point += 2
        elif i in "0123456789":
            point += 3
        elif i in "!@#$":
            point += 5
        # print(i, point)
    return point


password = "aA1!"
password = "bbB11#"
print(passwordStrength(password))
