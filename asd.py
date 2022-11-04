def maxPosPrefixes(arr):
    countZero = 0
    arr.sort()
    # print(arr)
    # for i in arr:
    #     if i < 0:
    #         num = arr[i]
    #         arr.pop(i)
    #         arr.append(num)
    # print(arr)
    res = 0
    sumNum = 0
    for i in reversed(arr):
        sumNum += i
        if sumNum > 0:
            res += 1
        else:
            break
    return res


def slotWheels(history):
    for i in range(len(history)):
        history[i] = list(history[i])
    totalStop = 0

    for _ in range(len(history[0])):
        overallMax = 0
        for j in range(len(history)):
            row = history[j]
            tempMax = 0
            maxIndex = 0
            for i in range(len(row)):
                if int(row[i]) > tempMax:
                    tempMax = int(row[i])
                    maxIndex = i

            #  = row[:maxIndex] + row[maxIndex+1: len(row)]
            history[j].pop(maxIndex)

            overallMax = max(tempMax, overallMax)

        print(history)
        totalStop += overallMax
    return totalStop

history = ['137', '364', '115', '724']
print(slotWheels(history))