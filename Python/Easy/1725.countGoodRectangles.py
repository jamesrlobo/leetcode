# 1725. Number Of Rectangles That Can Form The Largest Square
def countGoodRectangles(rectangles):
    maxLen = []
    for i in rectangles:
        maxLen.append(min(i[0], i[1]))
    return maxLen.count(max(maxLen))



# rectangles = [[5,8],[3,9],[5,12],[16,5]]
# rectangles = [[2,3],[3,7],[4,3],[3,7]]
rectangles = [[5,8],[3,9],[3,12]]
print(countGoodRectangles(rectangles))
