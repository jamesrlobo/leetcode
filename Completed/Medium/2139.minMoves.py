# 2139. Minimum Moves to Reach Target Score
# Beats: 16.45%
def minMoves(target, maxDoubles):
    steps = 0
    print(target, steps)
    while target != 1:
        if maxDoubles > 0 and target%2 != 0:
            target -= 1
            steps += 1
            print(target, steps)
        if maxDoubles > 0 and target//2 > 0:
            target = target//2
            steps += 1
            maxDoubles -= 1
            print(target, steps, "Done")
            if target == 1:
                return steps
        elif maxDoubles == 0:
            steps += target - 1
            target = 1
            print(target, steps)
    return steps


target = 5
maxDoubles = 0

target = 19
maxDoubles = 2

target = 10
maxDoubles = 4

target = 656101987
maxDoubles = 1

print(minMoves(target, maxDoubles))


# def minMoves(target, maxDoubles):
#     x = 1
#     steps = 0
#     while x < target:
#         if maxDoubles > 0 and x*2 <= target:
#             x = 2 * x
#         else:
#             x += 1
#         steps += 1
#     return steps
