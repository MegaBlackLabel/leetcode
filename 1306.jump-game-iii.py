#
# @lc app=leetcode id=1306 lang=python3
#
# [1306] Jump Game III
#

# @lc code=start
from collections import deque


class Solution:
    def canReach(self, arr: list[int], start: int) -> bool:
        queue = deque([start])
        visited = {start}
        
        while queue:
            curr = queue.popleft()
            
            if arr[curr] == 0:
                return True
                
            for next_idx in (curr + arr[curr], curr - arr[curr]):
                if 0 <= next_idx < len(arr) and next_idx not in visited:
                    visited.add(next_idx)
                    queue.append(next_idx)
                    
        return False
# @lc code=end

