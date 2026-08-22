# 2303. Calculate Amount Paid in Taxes
# Beats: 100.00%
def calculateTax(brackets, income):
    output, prev = 0, 0
    for i in range(len(brackets)):
        # print((min(brackets[i][0], income)-prev) * brackets[i][1]/100)
        output += (min(brackets[i][0], income)-prev) * brackets[i][1]/100
        prev = brackets[i][0]
        if income-prev<=0:
            break
    return output


brackets = [[3,50],[7,10],[12,25]]
income = 10

brackets = [[1,0],[4,25],[5,50]]
income = 2

brackets = [[2,50]]
income = 0
print(calculateTax(brackets, income))
