# 3285. Find Indices of Stable Mountains
def stableMountains(height, threshold):
    output = []
    i = 1
    while i < len(height):
        if height[i-1] > threshold:
            output.append(i)
        i+=1
    return output


# height = [1,2,3,4,5]
# threshold = 2
# height = [10,1,10,1,10]
# threshold = 3
height = [10,1,10,1,10]
threshold = 10
print(stableMountains(height, threshold))
