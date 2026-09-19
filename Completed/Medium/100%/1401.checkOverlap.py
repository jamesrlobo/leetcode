def checkOverlap(radius, xCenter, yCenter, x1, y1, x2, y2):
    # Step 1: Clamp the circle's center to the rectangle's boundaries
    # This finds the closest point \((x_n, y_n)\) on or inside the rectangle to the circle's center.
    xn = max(x1, min(xCenter, x2))
    yn = max(y1, min(yCenter, y2))
    # Step 2: Calculate the distance components
    # Find the horizontal and vertical distance from the circle's center to this closest point:
    deltax = xCenter - xn
    deltay = yCenter - yn
    # Step 3: Check the overlap condition
    # The shapes overlap if the squared distance is less than or equal to the squared radius:
    return ((deltax**2)+(deltay**2) <= (radius**2))


radius = 1
xCenter = 0
yCenter = 0
x1 = 1
y1 = -1
x2 = 3
y2 = 1

radius = 1
xCenter = 1
yCenter = 1
x1 = 1
y1 = -3
x2 = 2
y2 = -1

radius = 1
xCenter = 0
yCenter = 0
x1 = -1
y1 = 0
x2 = 0
y2 = 1
print(checkOverlap(radius, xCenter, yCenter, x1, y1, x2, y2))
