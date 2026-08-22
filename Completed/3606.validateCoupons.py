# 3606. Coupon Code Validator
# Beats: 45.66%
def validateCoupons(code, businessLine, isActive):
    output, output2 = [], []
    valid = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_'
    for i in range(len(code)):
        if isActive[i] == True and businessLine[i] in ["electronics", "grocery", "pharmacy", "restaurant"]:
            if code[i] != "":
                for j in code[i]:
                    if j not in valid:
                        break
                else:
                    output.append([businessLine[i],code[i]])
    output = sorted(output)
    for k in output:
        output2.append(k[1])
    return output2


code = ["1OFw","0MvB"]
businessLine = ["electronics","pharmacy"]
isActive = [True,True]

# code = ["rm"]
# businessLine = ["pharmacy"]
# isActive = [True]

# code = ["SAVE20","","PHARMA5","SAVE@20"]
# businessLine = ["restaurant","grocery","pharmacy","restaurant"]
# isActive = [True,True,True,True]
#
# code = ["GROCERY15","ELECTRONICS_50","DISCOUNT10"]
# businessLine = ["grocery","electronics","invalid"]
# isActive = [False,True,True]

print(validateCoupons(code, businessLine, isActive))
