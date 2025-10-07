#
# @lc app=leetcode id=816 lang=python3
#
# [816] Ambiguous Coordinates
#

# @lc code=start
from typing import List


class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        
        def generate(s):
            if len(s) == 1 or s[0] != '0':
                yield s
            for i in range(1, len(s)):
                if (s[0] != '0' or i == 1) and s[-1] != '0':
                    yield s[:i] + '.' + s[i:]

        s = s[1:-1]
        n = len(s)
        ans = []
        for i in range(1, n):
            for a in generate(s[:i]):
                for b in generate(s[i:]):
                    ans.append('({}, {})'.format(a, b))
        return ans
# @lc code=end

