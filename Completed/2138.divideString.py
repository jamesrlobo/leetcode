# 2138. Divide a String Into Groups of Size k
def divideString(s, k, fill):
    output = []
    l = len(s)
    i = 0
    while i < l:
        output.append(s[i:i+k])
        i+=k
    for x in output:
        if len(x) < 3:
            for y in range(k - len(x)):
                x += fill
    output[len(output)-1] = x
    return output


s = "abcdefghi"
k = 3
fill = "x"
s = "abcdefghij"
k = 3
fill = "x"
print(divideString(s, k, fill))
