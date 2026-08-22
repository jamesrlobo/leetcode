# 2037. Minimum Number of Moves to Seat Everyone
def minMovesToSeat(seats, students):
    output = 0
    seats.sort()
    students.sort()
    for i, j in zip(seats, students):
        output += abs(i-j)
    return output


# seats = [3,1,5]
# students = [2,7,4]
# seats = [4,1,5,9]
# students = [1,3,2,6]
seats = [2,2,6,6]
students = [1,3,2,6]
print(minMovesToSeat(seats, students))
