# 3668. Restore Finishing Order
def recoverOrder(order, friends):
    output = []
    for i in order:
        if i in friends:
            output.append(i)
    return output


order = [3,1,2,5,4]
friends = [1,3,4]
print(recoverOrder(order, friends))
