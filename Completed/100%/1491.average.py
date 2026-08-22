# 1491. Average Salary Excluding the Minimum and Maximum Salary
# Beats: 100.00%
def average(salary):
    total = sum(salary)
    maximum = max(salary)
    minimum = min(salary)
    return (total - (maximum + minimum)) / (len(salary)-2)


salary = [4000,3000,1000,2000]
salary = [1000,2000,3000]
print(average(salary))
