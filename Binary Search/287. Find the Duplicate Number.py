class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # This is a Linked-List problem, find the beginning of cycle
        # each nums[i] is i's next
        # apply Floyd's Algorithm

        fast, slow = nums[nums[0]], nums[0]
        while nums[fast] != nums[slow]:
            fast = nums[nums[fast]]
            slow = nums[slow]

        slow2 = 0
        while nums[slow] != nums[slow2]:
            slow2 = nums[slow2]
            slow = nums[slow]

        return nums[slow]