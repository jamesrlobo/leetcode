# 3184. Count Pairs That Form a Complete Day I
# Beats: 5.60%
def countCompleteDayPairs(hours):
    output = []
    for i in range(len(hours)):
        for j in range(len(hours)):
            if i < j:
                if (hours[i] + hours[j])%24 == 0:
                    output.append((i, j))
    return len(output)


# hours = [12,12,30,24,24]
hours = [72,48,24,3]
print(countCompleteDayPairs(hours))
