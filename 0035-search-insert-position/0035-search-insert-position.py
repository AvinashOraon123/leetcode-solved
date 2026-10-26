class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        n = len(nums)
        if n == 0:
            return 0
        low = 0
        high = n-1
        
        while low <= high:
            middle = (low+high)//2
            if nums[middle] < target:
                low = middle+1

            elif nums[middle] > target:
                high = middle-1
            else:
                return middle
  
        return low