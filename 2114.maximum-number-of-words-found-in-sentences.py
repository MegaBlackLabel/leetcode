#
# @lc app=leetcode id=2114 lang=python3
#
# [2114] Maximum Number of Words Found in Sentences
#

# @lc code=start
from typing import List


class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        return max(s.count(' ') for s in sentences) + 1
    
# @lc code=end

