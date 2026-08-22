# 925. Long Pressed Name
# https://leetcode.com/problems/traffic-signal-color/description/
# Beats: 100.00%
def isLongPressedName(name, typed):
    for i in set(name):
        if name.count(i) <= typed.count(i):
            continue
        else:
            return False
    return True


name = "alex"
typed = "aaleex"

name = "saeed"
typed = "ssaaedd"

name = "vtkgn"
typed = "vttkgnn"

name = "alex"
typed = "aaleexa"

name = "a"
typed = "b"

name = "rick"
typed = "kric"
print(isLongPressedName(name, typed))
