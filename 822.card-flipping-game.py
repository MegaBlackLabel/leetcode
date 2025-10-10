#
# @lc app=leetcode id=822 lang=python3
#
# [822] Card Flipping Game
#

# @lc code=start
from typing import List


class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        
        same = {f for f, b in zip(fronts, backs) if f == b}
        ans = min(
            (x for x in fronts + backs if x not in same),
            default=0
        )
        return ans if ans != float('inf') else 0
# @lc code=end

