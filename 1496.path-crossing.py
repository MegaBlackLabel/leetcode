#
# @lc app=leetcode id=1496 lang=python3
#
# [1496] Path Crossing
#

# @lc code=start
class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x, y = 0, 0
        visited = {(0, 0)}
      
        for direction in path:
            if direction == 'N':
                x -= 1
            elif direction == 'S':
                x += 1
            elif direction == 'E':
                y += 1
            elif direction == 'W':
                y -= 1
          
            if (x, y) in visited:
                return True
          
            visited.add((x, y))
      
        return False
    
# @lc code=end

