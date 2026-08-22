# 367. Valid Perfect Square
#Beats: 15.63%
def isPerfectSquare(num):
    if num < 2:
        return True
    low = 2
    high = num//2
    while low <= high:
        mid = (low+high)//2
        square = mid**2
        if square == num:
            return True
        elif num < square:
            high = mid-1
        else:
            low = mid+1
    return False


num = 14
print(isPerfectSquare(num))
