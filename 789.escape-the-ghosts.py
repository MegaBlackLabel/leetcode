#
# @lc app=leetcode id=789 lang=python3
#
# [789] Escape The Ghosts
#

# @lc code=start
from typing import List


class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        
        distance = abs(target[0]) + abs(target[1])

        for ghost in ghosts:
            ghost_distance = abs(ghost[0] - target[0]) + abs(ghost[1] - target[1])

            if ghost_distance <= distance:
                return False

        return True
# @lc code=end

