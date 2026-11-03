class Solution:
    def canJump(self, nums: list[int]) -> bool:
        reachable = 0
        for i, jump in enumerate(nums):
            if i> reachable:
                return False
            reachable = max(reachable, i+jump)
            if reachable >= len(nums)+1:
                return True
        return True
