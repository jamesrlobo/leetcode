# 2073. Time Needed to Buy Tickets
# Beats: 51.17%
def timeRequiredToBuy(tickets, k):
    seconds = 0
    while tickets[k] != 0:
        for i in range(len(tickets)):
            if tickets[k] == 0:
                return seconds
            if tickets[i] > 0:
                tickets[i] = tickets[i]-1
                seconds +=1
            else:
                continue
        print(tickets, seconds)
    return seconds


# tickets = [2,3,2]
# k = 2
# tickets = [5,1,1,1]
# k = 0
tickets = [84,49,5,24,70,77,87,8]
k = 3
print(timeRequiredToBuy(tickets, k))
