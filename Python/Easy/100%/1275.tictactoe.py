# 1275. Find Winner on a Tic Tac Toe Game
# https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/description/
# Beats: 100.00%
def tictactoe(self, moves: list[list[int]]) -> str:
    board = [["","",""], ["","",""], ["","",""]]
    turn = 0
    curr = ""
    for move in moves:
        row = move[0]
        col = move[1]
        if turn % 2 == 0:
            board[row][col] = "X"
            curr = "A"
        else:
            curr = "B"
            board[row][col] = "O"
        if turn > 3:
            diagonal1 = [board[0][0], board[1][1], board[2][2]]
            diagonal2 = [board[0][2], board[1][1], board[2][0]]
            firstcol = [board[0][0], board[1][0], board[2][0]]
            secondcol = [board[0][1], board[1][1], board[2][1]]
            thirdcol = [board[0][2], board[1][2], board[2][2]]
            # print(board[0], board[2], diagonal1, diagonal2, firstrow, secondrow)
            if board[0] == ['X', 'X', 'X'] or board[0] == ['O', 'O', 'O']:
                return curr
            elif board[1] == ['X', 'X', 'X'] or board[2] == ['O', 'O', 'O']:
                return curr
            elif board[2] == ['X', 'X', 'X'] or board[2] == ['O', 'O', 'O']:
                return curr
            elif diagonal1 == ['X', 'X', 'X'] or diagonal1 == ['O', 'O', 'O']:
                return curr
            elif diagonal2 == ['X', 'X', 'X'] or diagonal2 == ['O', 'O', 'O']:
                return curr
            elif firstcol == ['X', 'X', 'X'] or firstcol == ['O', 'O', 'O']:
                return curr
            elif secondcol == ['X', 'X', 'X'] or secondcol == ['O', 'O', 'O']:
                return curr
            elif thirdcol == ['X', 'X', 'X'] or thirdcol == ['O', 'O', 'O']:
                return curr
        turn += 1
    # print(board)
    if turn < 9:
        return "Pending"
    return "Draw"
