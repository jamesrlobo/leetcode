# 1700. Number of Students Unable to Eat Lunch
# Beats: 100.00%
def countStudents(students, sandwiches):
    i = 0
    while i < len(students):
        if students[i] == sandwiches[0]:
            students.pop(i)
            sandwiches.pop(0)
            i = 0
        else:
            i+=1
    return len(students)


# students = [1,1,0,0]
# sandwiches = [0,1,0,1]
# students = [1,1,1,0,0,1]
# sandwiches = [1,0,0,0,1,1]
# students = [1,0,1,0,1,1,0,1,1,1,1,0,0,0,1,1,1,0,1,1,1,1,0,0,0,1,0,0,0,0]
# sandwiches = [0,1,0,0,1,1,1,1,1,1,0,1,1,0,0,0,1,1,0,0,1,1,1,1,0,0,1,0,1,0]
students = [0,0,0,1,1,1,1,0,0,0]
sandwiches = [1,0,1,0,0,1,1,0,0,0]
print(countStudents(students, sandwiches))
