# 2833. Furthest Point From Origin
# https://leetcode.com/problems/furthest-point-from-origin/description/
# Beats: 100.00%
def furthestDistanceFromOrigin(moves):
    output = 0
    moves = list(moves)
    if moves.count("L") > moves.count("R"):
        for i in range(len(moves)):
            if moves[i] == "_":
                moves[i] = "L"
    else:
        for j in range(len(moves)):
            if moves[j] == "_":
                moves[j] = "R"
    for move in moves:
        if move == "L":
            output += 1
        else:
            output -= 1
    return abs(output)


moves = "L_RL__R"
moves = "_R__LL_"
moves = "_______"
print(furthestDistanceFromOrigin(moves))
