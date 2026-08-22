def decrypt(code, k):
    output = [0] * len(code)
    if k == 0:
        return output
    if k > 0:
        turn = 0
        while turn < len(code):
            output[turn] = sum(code[1:k+1])
            temp = code.pop(0)
            code.append(temp)
            print(code, output)
            turn +=1
    else:
        code = code[::-1]
        turn = 0
        while turn < len(code):
            output[turn] = sum(code[1:k+1])
            temp = code.pop(0)
            code.append(temp)
            print(code, output)
            turn +=1
        output = output[::-1]
    return output

# code = [5,7,1,4]
# k = 3
# code = [1,2,3,4]
# k = 0
code = [2,4,9,3]
k = -2
print(decrypt(code, k))
