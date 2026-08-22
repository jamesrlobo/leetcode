# 2180. Count Integers With Even Digit Sum
def countEven(num):
    output = [x for x in range(2, num+1)]
    i = 0
    while i < len(output):
        if output[i] < 10 and output[i]%2 != 0:
            output.pop(i)
        elif output[i] > 9:
            temp = 0
            for j in range(len(str(output[i]))):
                temp += int(str(output[i])[j])
            if temp%2 != 0:
                output.pop(i)
            else:
                i+=1
        else:
            i+=1
    return len(output)


num = 30
# num = 4
print(countEven(num))
