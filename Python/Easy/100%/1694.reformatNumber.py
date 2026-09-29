# 1694. Reformat Phone Number
# Beats: 100.00%
def reformatNumber(number):
    output, result = [], []
    text = [x for x in number if x.isalnum()]
    i = 0
    while i < len(text):
        output.append(text[i:i+3])
        i+=3
    if len(output[-1]) == 1:
        temp = output[-2] + output[-1]
        output.pop(-1)
        output.pop(-1)
        j = 0
        while j < len(temp):
            output.append(temp[j:j+2])
            j+=2
    for k in output:
        result.append("".join(k))
    return "-".join(result)

number = "1-23-45 6"
# number = "123 4-567"
# number = "123 4-5678"
print(reformatNumber(number))
