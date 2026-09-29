# 3274. Check if Two Chessboard Squares Have the Same Color
# https://leetcode.com/problems/check-if-two-chessboard-squares-have-the-same-color/description/
# Beats: 70.96%
def checkTwoChessboards(coordinate1, coordinate2):
    c1 = (int(ord(coordinate1[0])) + int(coordinate1[1]))%2
    c2 = (int(ord(coordinate2[0])) + int(coordinate2[1]))%2
    if c1 == c2:
        return True
    return False


coordinate1 = "a1"
coordinate2 = "c3"
print(checkTwoChessboards(coordinate1, coordinate2))
