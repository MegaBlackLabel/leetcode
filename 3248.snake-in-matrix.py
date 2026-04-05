#
# @lc app=leetcode id=3248 lang=python3
#
# [3248] Snake in Matrix
#

# @lc code=start
from typing import List


class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        r, c = 0, 0
        
        for cmd in commands:
            if cmd == "UP": 
                r -= 1
            elif cmd == "DOWN": 
                r += 1
            elif cmd == "LEFT": 
                c -= 1
            elif cmd == "RIGHT": 
                c += 1
        return r * n + c
# @lc code=end

