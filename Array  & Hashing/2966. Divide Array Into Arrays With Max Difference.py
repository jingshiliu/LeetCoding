def divideArray(nums: list, k: int) -> list[list[int]]:
    # one pass
    # track min and max in current sub array
    # start a new array if max and min failed to maintain the difference
    # if found a number that cannot maintain the diff with next num and prev num, return []
    nums.sort()
    res, cur = [], []
    cur_min, cur_max = 99999, 0
    for num in nums:
        if cur_max - cur_min <= k:
            cur.append(num)
        elif len(cur) > 1:
            res.append(cur)
        else:
            return []
                
        if res and (res[-1] == cur or len(cur) == 3):
            cur = [num]
            cur_min, cur_max = num, num

    res.append(cur)
    return res


numbers = [1,3,4,8,7,9,3,5,1]
result = divideArray(numbers, 2)
print(result)