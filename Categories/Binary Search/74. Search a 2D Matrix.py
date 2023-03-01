def searchMatrix( matrix: list[list[int]], target: int) -> bool:
    # nested bin search
    l, r = 0, len(matrix)

    # n = len(matrix)  m = len(row)
    while l < r:  # O(logn)
        cur = (l + r) // 2
        if matrix[cur][0] <= target <= matrix[cur][-1]:
            # O(logm)
            l2, r2 = 0, len(matrix[cur])

            while l2 < r2:
                cur2 = (l2 + r2) // 2

                if matrix[cur][cur2] == target:
                    return True
                if matrix[cur][cur2] < target:
                    l2 = cur2 + 1
                else:
                    r2 = cur2
            return False

        if matrix[cur][0] < target:
            l = cur + 1
        else:
            r = cur
    return False