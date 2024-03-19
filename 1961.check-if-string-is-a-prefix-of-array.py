#
# @lc app=leetcode id=1961 lang=python3
#
# [1961] Check If String Is a Prefix of Array
#

# @lc code=start
from typing import List


class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        prefix = []
    
        for word in words:
            prefix.append(word)
            if ''.join(prefix) == s:
                return True
        return False
# @lc code=end

