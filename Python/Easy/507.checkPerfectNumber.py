# 507. Perfect Number
def checkPerfectNumber(num):
    if num<=1:
        return False
    sumdiv=1
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            sumdiv+=i
            if i*i!=num:
                sumdiv+=num//i
    return sumdiv==num

num = 99999998
print(checkPerfectNumber(num))


# def checkPerfectNumber(num):
#     total = 0
#     for i in range(1, num):
#         if num%i == 0:
#             total += i
#     if total == num:
#         return True
#     else:
#         return False
