# 2264. Largest 3-Same-Digit Number in String
# Beats: 100.00%
def largestGoodInteger(num):
    if "999" in num:
        return "999"
    elif "888" in num:
        return "888"
    elif "777" in num:
        return "777"
    elif "666" in num:
        return "666"
    elif "555" in num:
        return "555"
    elif "444" in num:
        return "444"
    elif "333" in num:
        return "333"
    elif "222" in num:
        return "222"
    elif "111" in num:
        return "111"
    elif "000" in num:
        return "000"
    else:
        return ""


# num = "677713333999"
num = "2300019"
# num = "42352338"
print(largestGoodInteger(num))

# def largestGoodInteger(num):
#     output = ""
#     n = -1
#     for i in range(len(num)-2):
#         if len(set(num[i:i+3])) == 1:
#             if int(num[i:i+3]) > n:
#                 n = int(num[i:i+3])
#                 output = num[i:i+3]
#     return output
