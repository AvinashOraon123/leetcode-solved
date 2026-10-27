class Solution:

    def lower_bound(self, nums, target):
        n = len(nums)
        lb = n
        l, h = 0, n - 1

        while l <= h:
            m = (l + h) // 2
            if nums[m] >= target:
                lb = m
                h = m - 1
            else:
                l = m + 1
        return lb

    def upper_bound(self, nums, target):
        n = len(nums)
        ub = n
        l, h = 0, n - 1

        while l <= h:
            m = (l + h) // 2
            if nums[m] > target:
                ub = m
                h = m - 1
            else:
                l = m + 1
        return ub

    def searchRange(self, nums: list[int], target: int) -> list[int]:
        lb = self.lower_bound(nums, target)
        if lb == len(nums) or nums[lb] != target:
            return [-1, -1]

        return [lb, self.upper_bound(nums, target) - 1]