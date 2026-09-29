# 682. Baseball Game
def calPoints(ops):
    record = []
    for i in ops:
        if i.isdigit():
            record.append(int(i))
        elif i.isalpha():
            if i == "C":
                record.pop()
            elif i == "D":
                record.append(record[-1]*2)
        else:
            if i == "+":
                record.append(sum(record[len(record)-2:]))
            else:
                record.append(int(i))
    return sum(record)


# ops = ["5","2","C","D","+"]
ops = ["5","-2","4","C","D","9","+","+"]
# ops = ["1","C"]
print(calPoints(ops))
