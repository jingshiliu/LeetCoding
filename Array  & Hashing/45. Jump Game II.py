class Solution:
    def jump(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return 0
        i = 0
        boundary = nums[0]
        jump = 1

        while i < len(nums):
            # each iter means one jump
            # we want to find the second jump within the range of current jump that bring us the furthest
            if boundary >= len(nums) - 1:
                break
                
            max_boundary = boundary
            while i <= boundary:
                max_boundary = max(nums[i] + i, max_boundary)
                i += 1
            boundary = max_boundary
            jump += 1

        return jump
    

nums = [2,3,1,1,4]
print(Solution().jump(nums))