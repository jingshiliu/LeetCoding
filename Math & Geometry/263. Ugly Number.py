def is_ugly(n):
    """
    Time complexity: O(logn)
        we are dividng the integer by 2, 3, 5 and termincating when it is not divisible
        when dividing an integer x by y, there are at most logy(x) divisions
    """
    # remove all 2, 3, 5 from the N
    # if there is another prime factor left, means is not ugly
    # else the leftover must be 1

    while n > 1:
        if n % 2 == 0:
            n /= 2
        elif n % 3 == 0:
            n /= 3
        elif n % 5 == 0:
            n /= 5
        else:
            return False
    return n == 1