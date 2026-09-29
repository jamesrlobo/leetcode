# 836. Rectangle Overlap
# https://leetcode.com/problems/rectangle-overlap/description/
# Beats: 100.00%
def isRectangleOverlap(rec1, rec2):
    rec1_x1 = rec1[0]
    rec1_y1 = rec1[1]
    rec1_x2 = rec1[2]
    rec1_y2 = rec1[3]
    rec2_x1 = rec2[0]
    rec2_y1 = rec2[1]
    rec2_x2 = rec2[2]
    rec2_y2 = rec2[3]
    # Overlap = (A_x1 < B_x2) AND (A_x2 > B_x1) AND (A_y1 < B_y2) AND (A_y2 > B_y1)
    overlap = (rec1_x1 < rec2_x2) and (rec1_x2 > rec2_x1) and (rec1_y1 < rec2_y2) and (rec1_y2 > rec2_y1)
    return overlap


rec1 = [0,0,2,2]
rec2 = [1,1,3,3]

rec1 = [0,0,1,1]
rec2 = [1,0,2,1]

rec1 = [0,0,1,1]
rec2 = [2,2,3,3]
print(isRectangleOverlap(rec1, rec2))
