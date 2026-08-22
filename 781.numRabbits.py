# 781. Rabbits in Forest
def numRabbits(answers):
    output = 0
    d = {}
    for i in range(len(answers)):
        if answers[i] not in d:
            d[answers[i]] =  answers.count(answers[i])
        else:
            d[answers[i]] + answers.count(answers[i])
    print(d)


answers = [1,1,2]
# answers = [10,10,10]
# answers = [1,0,1,0,0]
# answers = [0,0,1,1,1]
print(numRabbits(answers))
