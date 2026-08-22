def generate(numRows):
    output = [[1]]
    for i in range(2, numRows+1):
        print(output[-1]*i)
    return


numRows = 5
print(generate(numRows))
