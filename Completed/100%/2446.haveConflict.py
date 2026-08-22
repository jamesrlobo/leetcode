# 2446. Determine if Two Events Have Conflict
# Beats: 100.00%
def haveConflict(event1, event2):
    ev1start = event1[0].replace(":", "")
    ev1start = (int(ev1start[:2]))*60 + int(ev1start[2:])
    ev1end = event1[1].replace(":", "")
    ev1end = (int(ev1end[:2]))*60 + int(ev1end[2:])
    print(ev1start, ev1end)
    ev2start = event2[0].replace(":", "")
    ev2start = (int(ev2start[:2]))*60 + int(ev2start[2:])
    ev2end = event2[1].replace(":", "")
    ev2end = (int(ev2end[:2]))*60 + int(ev2end[2:])
    print(ev2start, ev2end)
    if ev1end >= ev2start and ev1start <= ev2start:
        return True
    if ev2start <= ev1end and ev2end >= ev1start:
        return True
    return False


event1 = ["14:13","22:08"]
event2 = ["02:40","08:08"]

event1 = ["01:15","02:00"]
event2 = ["02:00","03:00"]

event1 = ["01:00","02:00"]
event2 = ["01:20","03:00"]

event1 = ["10:00","11:00"]
event2 = ["14:00","15:00"]
print(haveConflict(event1, event2))
