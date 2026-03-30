#
# @lc app=leetcode id=3222 lang=python3
#
# [3222] Find the Winning Player in Coin Game
#

# @lc code=start
class Solution:
    def winningPlayer(self, x: int, y: int) -> str:
        max_turns = min(x, y // 4)
        
        return "Alice" if max_turns % 2 == 1 else "Bob"
# @lc code=end

