#
# @lc app=leetcode id=1222 lang=python3
#
# [1222] Queens That Can Attack the King
#

# @lc code=start
class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        queen_set = {tuple(q) for q in queens}
        result = []
        
        directions = [
            (-1, 0), (1, 0), (0, -1), (0, 1),
            (-1, -1), (-1, 1), (1, -1), (1, 1)
        ]
        
        for dx, dy in directions:
            x, y = king
            while 0 <= x + dx < 8 and 0 <= y + dy < 8:
                x += dx
                y += dy
                if (x, y) in queen_set:
                    result.append([x, y])
                    break
                    
        return result
# @lc code=end

