# 3386. Button with Longest Push Time
# Beats: 11.87%
def buttonWithLongestTime(events):
    time = events[0][1]
    index = 0
    print(time, index)
    for i in range(1, len(events)):
        print(f'Time: {abs(events[i-1][1] - events[i][1])} and time:{time}', events[i])
        if abs(events[i-1][1] - events[i][1]) == time:
            if events[i] < events[index]:
                index = i
        elif abs(events[i-1][1] - events[i][1]) > time:
            time = abs(events[i-1][1] - events[i][1])
            index = i
        print(time, index)
    return events[index][0]


events = [[1,2],[2,5],[3,9],[1,15]]
events = [[10,5],[1,7]]
events = [[1,5],[19,9],[6,10],[6,11],[16,14],[1,16],[15,19]]
events = [[9,4],[19,5],[2,8],[3,11],[2,15]]
events = [[1,4],[18,5],[15,7],[12,9],[1,11],[18,13],[16,17]]
print(buttonWithLongestTime(events))
