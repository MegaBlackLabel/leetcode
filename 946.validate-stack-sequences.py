#
# @lc app=leetcode id=946 lang=python3
#
# [946] Validate Stack Sequences
#

# @lc code=start
from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        
        stack = []
        j = 0

        for value in pushed:
            stack.append(value)

            while stack and stack[-1] == popped[j]:
                stack.pop()
                j += 1

        return not stack
# @lc code=end

