# 925. Long Pressed Name
# https://leetcode.com/problems/long-pressed-name/
# Beats: 100.00%
def isLongPressedName(self, name: str, typed: str) -> bool:
    typed_count, name_count = [], []
    count = 1
    if len(typed) == 1:
        typed_count.append([typed, 1])
    else:
        for i in range(1, len(typed)):
            if typed[i-1] != typed[i]:
                typed_count.append([typed[i-1], count])
                count = 1
            else:
                count += 1
        typed_count.append([typed[i], count])
    count = 1
    if len(name) == 1:
        name_count.append([name, 1])
    else:
        for j in range(1, len(name)):
            if name[j-1] != name[j]:
                name_count.append([name[j-1], count])
                count = 1
            else:
                count += 1
        name_count.append([name[j], count])
    # print(typed_count)
    # print(name_count)
    if len(typed_count) != len(name_count):
        return False
    for k in range(len(typed_count)):
        if typed_count[k][0] == name_count[k][0] and typed_count[k][1] >= name_count[k][1]:
            continue
        else:
            return False
    return True
