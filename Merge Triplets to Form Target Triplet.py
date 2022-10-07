def mergeTriplets(self, triplets, target) -> bool:
    indexRecord = [0, 0, 0]
    triLen = len(target)
    triListLen = len(triplets)
    # Idea:
    # Find 0index first and move to next level
    # If found in next level, move further
    # Otherwise, go back to last level to find the rest in last level

    level = 0
    indexRecord[level] = 0
    resTri = [0] * 3
    while indexRecord[level] < triListLen:
        curTriplet = triplets[indexRecord[level]]
        curVal = curTriplet[level]

        if curVal == target[level]:
            isValid = True

            for j in range(triLen):
                if j != level and curTriplet[j] > target[j]:
                    isValid = False
                    break
            if isValid:
                if level == triLen - 1:
                    return True
                # resTri = merge(curTriplet, resTri)
                for j in range(triLen):
                    resTri[j] = max(resTri[j], curTriplet[j])
                indexRecord[level] = indexRecord[level]
                level += 1
                continue
        elif indexRecord[level] == triListLen:
            level -= 1
            if level == -1:
                return False
            indexRecord[level] = indexRecord[level]

        indexRecord[level] += 1

    return False