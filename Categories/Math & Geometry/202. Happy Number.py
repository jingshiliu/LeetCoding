class Solution:
    def isHappy(self, n: int) -> bool:
        numsCalculated = set()

        while n != 1:
            if n in numsCalculated:
                return False
            numsCalculated.add(n)
            cur = 0
            for i in str(n):
                cur += int(i) ** 2
            n = cur
        return True