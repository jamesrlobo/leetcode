# 1507. Reformat Date
def reformatDate(date):
    output = ""
    words = date.split(" ")
    words = words[::-1]
    month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    if len(str(month.index(words[1])+1)) == 1:
        output += words[0] + "-" + '0'+str(month.index(words[1])+1) + "-"
    else:
        output += words[0] + "-" + str(month.index(words[1])+1) + "-"
    date = ""
    for i in words[2]:
        if str(i).isdigit():
            date +=i
    if len(date) == 1:
        output += "0"+date
    else:
        output += date
    return output


# date = "20th Oct 2052"
# date = "6th Jun 1933"
date = "26th May 1960"
print(reformatDate(date))
