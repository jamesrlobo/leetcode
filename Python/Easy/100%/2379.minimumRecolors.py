# 2379. Minimum Recolors to Get K Consecutive Black Blocks
# https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/description/
# Beats: 100.00%
def minimumRecolors(blocks, k):
    n = len(blocks)
    output = []
    for i in range(n-k+1):
        # print(blocks[i:i+k].count("W"))
        output.append(blocks[i:i+k].count("W"))
    return min(output)


blocks = "WBBWWBBWBW"
k = 7
blocks = "WBWBBBW"
k = 2
print(minimumRecolors(blocks, k))
