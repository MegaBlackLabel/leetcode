#
# @lc app=leetcode id=1023 lang=python3
#
# [1023] Camelcase Matching
#

# @lc code=start
from typing import List


class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        
        def match(query: str) -> bool:
            i = 0
            for c in query:
                if i < len(pattern) and c == pattern[i]:
                    i += 1
                elif c.isupper():
                    return False
            return i == len(pattern)

        return [match(query) for query in queries]
# @lc code=end

