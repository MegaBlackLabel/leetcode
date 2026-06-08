#
# @lc app=leetcode id=1040 lang=python3
#
# [1040] Moving Stones Until Consecutive II
#

# @lc code=start
class Solution:
    def numMovesStonesII(self, stones: List[int]) -> List[int]:
        stones.sort()
        n = len(stones)
        
        max_moves = (stones[-1] - stones[0] + 1 - n) - min(
            stones[1] - stones[0] - 1, 
            stones[-1] - stones[-2] - 1
        )
        
        min_moves = n
        left = 0
        
        for right in range(n):
            while stones[right] - stones[left] >= n:
                left += 1
            
            window_size = right - left + 1
            
            if window_size == n - 1 and stones[right] - stones[left] == n - 2:
                moves = 2
            else:
                moves = n - window_size
                
            min_moves = min(min_moves, moves)
            
        return [min_moves, max_moves]
# @lc code=end

