# 3280. Convert Date to Binary
def convertDateToBinary(date):
    output = []
    l = date.split("-")
    for i in l:
        output.append(bin(int(i))[2:])
    return "-".join(output)


date = "2080-02-29"
print(convertDateToBinary(date))
