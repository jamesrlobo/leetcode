# 1323. Maximum 69 Number
def maximum69Number(num):
    output = num
    num = str(num)
    i = 0
    while i < len(num):
        if num[i] == '9':
            output = max(output,int(num[:i]+'6'+num[i+1:]))
        else:
            output = max(output, int(num[:i]+'9'+num[i+1:]))
        i+=1
    return output


num = 9999
print(maximum69Number(num))
