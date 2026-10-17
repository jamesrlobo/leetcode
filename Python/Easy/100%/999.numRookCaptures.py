# 999. Available Captures for Rook
# https://leetcode.com/problems/available-captures-for-rook/description/
# Beats: 100.00%
def numRookCaptures(self, board: list[list[str]]) -> int:
    curr = (0,0)
    for i in range(8):
        if "R" in (board[i]):
            for j in range(8):
                if board[i][j] == "R":
                    curr = (i, j)
                    break
            break
    left = board[i][:j]
    right = board[i][j+1:]
    up, down = [], []
    for x in range(8):
        if x < i:
            up.append(board[x][j])
        elif x > i:
            down.append(board[x][j])
    left = left[::-1]
    up = up[::-1]
    output = 0
    positions = [left, right, up, down]
    for direction in positions:
        for m in direction:
            if m != ".":
                if m == "p":
                    output += 1
                    break
                else:
                    break
    return output
