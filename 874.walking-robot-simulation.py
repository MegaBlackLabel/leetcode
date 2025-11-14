#
# @lc app=leetcode id=874 lang=python3
#
# [874] Walking Robot Simulation
#

# @lc code=start
from typing import List


class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        dir_idx = 0
        x, y = 0, 0
        max_distance_sq = 0
        obstacle_set = set(map(tuple, obstacles))

        for command in commands:
            if command == -2:
                dir_idx = (dir_idx - 1) % 4
            elif command == -1:
                dir_idx = (dir_idx + 1) % 4
            else:
                for _ in range(command):
                    next_x = x + directions[dir_idx][0]
                    next_y = y + directions[dir_idx][1]
                    if (next_x, next_y) not in obstacle_set:
                        x, y = next_x, next_y
                        max_distance_sq = max(max_distance_sq, x * x + y * y)
                    else:
                        break

        return max_distance_sq
# @lc code=end

