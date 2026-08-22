# 2582. Pass the Pillow
#Beats: 12.31%
def passThePillow(n, time):
    # people = []
    # for i in range(1, n+1):
    #     people.append(i)
    # print(people)
    direction = True
    current = 0
    pos = 1
    while current != time:
        if direction == True:
            current += 1
            pos += 1
        else:
            current += 1
            pos -= 1
        if pos == n:
            direction = False
        if pos == 1:
            direction = True
        # print(current, pos)
    return pos


n = 4
time = 5

n = 3
time = 2

n = 18
time = 38
print(passThePillow(n, time))
