class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        n = len(nums)
        l , h = 0 , n-1
        while l <= h:
            m = (l+h)//2
            if nums[m] == target:
                return True
            if nums[l] == nums[m] == nums[h]:
                l+=1
                h-=1
                continue
            if nums[h]>=nums[m]:
                if nums[m]<target<=nums[h]:
                    l= m+1
                else:
                    h = m-1
            else:
                if nums[l]<=target< nums[m]:
                    h = m-1
                else:
                    l= m+1
        return False