class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [[101, -1]]  # [temperature, index]
        res = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while (t > stack[-1][0]):
                res[stack[-1][1]] = i - stack[-1][1]
                stack.pop()

            stack.append([t, i])

        return res