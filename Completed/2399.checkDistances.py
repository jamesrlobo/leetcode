# 2399. Check Distances Between Same Letters
# Beats: 37.82%
def checkDistances(s, distance):
    for i in set(s):
        temp = []
        for j in range(len(s)):
            if s[j] == i:
                temp.append(j)
        if(distance[ord(i)-97] != temp[1]-temp[0]-1):
            return False
    return True


# s = "abaccb"
# distance = [1,3,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
s = "aa"
distance = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
print(checkDistances(s, distance))
