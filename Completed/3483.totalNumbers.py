# 3483. Unique 3-Digit Even Numbers
# Beats: 7.52%
def totalNumbers(digits):
    possible, output = [], []
    minimum = max(100, int(str(min(digits))*3))
    maximum = int(str(max(digits))*3)
    print(minimum, maximum)
    for i in range(minimum, maximum):
        if i%2 == 0 and len(set(str(i))) == 3:
            for ch in range(len(str(i))):
                if int(str(i)[ch]) not in digits:
                    break
            else:
                possible.append(i)
    for x in possible:
        for y in str(x):
            if str(x).count(y) > digits.count(int(y)):
                break
        else:
            output.append(x)
    return len(output)


# digits = [1,2,3,4]
digits = [0,2,2]
print(totalNumbers(digits))
