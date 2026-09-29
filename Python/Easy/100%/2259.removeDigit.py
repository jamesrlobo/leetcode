# 2259. Remove Digit From Number to Maximize Result
# Beats: 100.00%
def removeDigit(number, digit):
    output = []
    for i in range(len(number)):
        string = ""
        if number[i] ==  digit:
            string += number[:i] + number[i+1:]
        if string != "":
            output.append(int(string))
    return str(max(output))


# number = "123"
# digit = "3"
# number = "1231"
# digit = "1"
number = "551"
digit = "5"
print(removeDigit(number, digit))
