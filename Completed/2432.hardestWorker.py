# 2432. The Employee That Worked on the Longest Task
def hardestWorker(n, logs):
    start_time = 0
    best_employee, highest_time_spent = 0, 0
    for i in range(len(logs)):
        employee_id = logs[i][0]
        time_spent = logs[i][1] - start_time
        start_time = logs[i][1]
        print("Emp ID:", employee_id)
        print("Units of Time Spent:", time_spent)
        if time_spent > highest_time_spent:
            highest_time_spent = time_spent
            best_employee = employee_id
        elif time_spent == highest_time_spent:
            if best_employee > employee_id:
                best_employee = employee_id
    return (best_employee)


# n = 10
# logs = [[0,3],[2,5],[0,9],[1,15]]
# n = 26
# logs = [[1,1],[3,7],[2,12],[7,17]]
n = 2
logs = [[1,10],[0,20]]
print(hardestWorker(n, logs))
