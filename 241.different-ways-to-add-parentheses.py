#
# @lc app=leetcode id=241 lang=python3
#
# [241] Different Ways to Add Parentheses
#

# @lc code=start
from typing import List


class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        ans = []

        for i, c in enumerate(expression):
            if c in '+-*':
                for a in self.diffWaysToCompute(expression[:i]):
                    for b in self.diffWaysToCompute(expression[i + 1:]):
                        ans.append(eval(str(a) + c + str(b)))

        return ans or [int(expression)]
# @lc code=end

