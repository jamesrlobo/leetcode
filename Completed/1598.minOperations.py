# 1598. Crawler Log Folder
def minOperations(logs):
    main = 0
    for i in range(len(logs)):
        if logs[i] == "../":
            if main-1 < 0:
                continue
            else:
                main -=1
        elif logs[i] == "./":
            continue
        elif logs[i][-1] == "/":
            main +=1
    return main


# logs = ["d1/","d2/","../","d21/","./"]
# logs = ["d1/","d2/","./","d3/","../","d31/"]
logs = ["d1/","../","../","../"]
print(minOperations(logs))
