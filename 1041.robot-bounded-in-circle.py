#
# @lc app=leetcode id=1041 lang=python3
#
# [1041] Robot Bounded In Circle
#

# @lc code=start
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        x, y = 0, 0
        idx = 0
        
        for instruction in instructions:
            if instruction == 'G':
                x += directions[idx][0]
                y += directions[idx][1]
            elif instruction == 'L':
                idx = (idx + 3) % 4
            elif instruction == 'R':
                idx = (idx + 1) % 4
                
        return (x, y) == (0, 0) or idx != 0
# @lc code=end

