#
# @lc app=leetcode id=1248 lang=python3
#
# [1248] Count Number of Nice Subarrays
#

# @lc code=start
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        return self.atMostK(nums, k) - self.atMostK(nums, k - 1)

    def atMostK(self, nums: list[int], k: int) -> int:
        if k < 0:
            return 0
            
        left = 0
        odd_count = 0
        subarrays = 0
        
        for right in range(len(nums)):
            if nums[right] % 2 != 0:
                odd_count += 1
                
            while odd_count > k:
                if nums[left] % 2 != 0:
                    odd_count -= 1
                left += 1
                
            subarrays += (right - left + 1)
            
        return subarrays
# @lc code=end

