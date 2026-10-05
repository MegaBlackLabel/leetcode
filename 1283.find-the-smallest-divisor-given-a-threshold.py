#
# @lc app=leetcode id=1283 lang=python3
#
# [1283] Find the Smallest Divisor Given a Threshold
#

# @lc code=start
class Solution:
    def smallestDivisor(self, nums: list[int], threshold: int) -> int:
        left, right = 1, max(nums)
        
        while left < right:
            mid = (left + right) // 2
            
            total_sum = sum((num + mid - 1) // mid for num in nums)
            
            if total_sum <= threshold:
                right = mid
            else:
                left = mid + 1
                
        return left
# @lc code=end

