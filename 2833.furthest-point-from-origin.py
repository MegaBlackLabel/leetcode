#
# @lc app=leetcode id=2833 lang=python3
#
# [2833] Furthest Point From Origin
#

# @lc code=start
class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        return abs(moves.count('L') - moves.count('R')) + moves.count('_')
# @lc code=end

