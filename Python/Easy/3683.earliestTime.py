# 3683. Earliest Time to Finish One Task
def earliestTime(tasks):
    output = tasks[0][0] + tasks[0][1]
    for i in range(len(tasks)):
        if output > tasks[i][0] + tasks[i][1]:
            output = tasks[i][0] + tasks[i][1]
    return output


tasks = [[1,6],[2,3]]
print(earliestTime(tasks))
