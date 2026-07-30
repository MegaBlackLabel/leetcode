#
# @lc app=leetcode id=1144 lang=python3
#
# [1144] Decrease Elements To Make Array Zigzag
#

# @lc code=start
class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        res = [0, 0]
        n = len(nums)
        
        for i in range(n):
           
            left = nums[i - 1] if i > 0 else float('inf')
            right = nums[i + 1] if i < n - 1 else float('inf')
            
          
            target_valley = min(left, right)
            
            if nums[i] >= target_valley:
                moves = nums[i] - target_valley + 1
                res[i % 2] += moves
                
        return min(res)
# @lc code=end

