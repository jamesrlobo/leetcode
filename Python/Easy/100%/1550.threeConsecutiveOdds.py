# 1550. Three Consecutive Odds
# Beats: 100.00%
def threeConsecutiveOdds(arr):
    for i in range(0, len(arr), 1):
        x = arr[i:i+3]
        if len(x) < 3:
            break
        print(x)
        for j in range(len(x)):
            if x[j]%2 == 0:
                break
        else:
            return True
    return False


# arr = [2,6,4,1]
arr = [1,2,34,3,4,5,7,23,12]
print(threeConsecutiveOdds(arr))
