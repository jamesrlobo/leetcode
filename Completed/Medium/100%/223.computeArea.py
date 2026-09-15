# 223. Rectangle Area
# https://leetcode.com/problems/rectangle-area/description/
# Beats: 100.00%
def computeArea(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
    areaA = (ax2-ax1) * (ay2-ay1)
    areaB = (bx2-bx1) * (by2-by1)
    overlap_width = min(ax2, bx2) - max(ax1, bx1)
    overlap_height = min(ay2, by2) - max(ay1, by1)
    if overlap_width > 0 and overlap_height > 0:
        overlap_area = overlap_width * overlap_height
    else:
        overlap_area = 0
    return areaA + areaB - overlap_area


ax1 = -3
ay1 = 0
ax2 = 3
ay2 = 4
bx1 = 0
by1 = -1
bx2 = 9
by2 = 2
print(computeArea(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2))
