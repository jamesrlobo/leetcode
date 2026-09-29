# 1304. Find N Unique Integers Sum up to Zero
def sumZero(n):
    output = []
    if n%2 == 0:
        i = 1
        while i<= n:
            output.append(i)
            output.append(-i)
            i+= 2
    else:
        i = 1
        while i<= n-1:
            output.append(i)
            output.append(-i)
            i+=2
        output.append(0)
    return output


# n = 4
n = 1
print(sumZero(n))
