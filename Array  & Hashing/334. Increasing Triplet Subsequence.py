def increasingTriplet(nums) -> bool:
    """
    Time: O(n)
    Space: O(1)
    Scan left to right
    first_num updated only if there is no smaller num on the left
    second_num updated only if there is a smaller num on the left
    'third_num' found if there are 2 smaller on the left
    """
    if len(nums) < 3: return False

    first_num, second_num = float('inf'), float('inf')

    for n in nums:
        if n <= first_num:
            first_num = n
        elif n <= second_num:
            second_num = n
        else:
            return True

    return False

def increasingTriplet1(nums) -> bool:
    """
    Time and Space: O(n)
    Scan from left to right to see if there is a smaller number on the left of each index
    Then do the same but find larger number from right to left
    """
    if len(nums) < 3: return False

    min_arr = [False for i in nums]
    cur_min = nums[0]
    for i in range(len(nums)):
        if cur_min >= nums[i]:
            cur_min = nums[i]
        else:
            min_arr[i] = True

    cur_max = nums[-1]
    for i in range(len(nums) - 1, -1, -1):
        if cur_max <= nums[i]:
            cur_max = nums[i]
        elif min_arr[i]:
            return True

    return False