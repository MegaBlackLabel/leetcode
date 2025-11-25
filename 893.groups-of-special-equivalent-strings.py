#
# @lc app=leetcode id=893 lang=python3
#
# [893] Groups of Special-Equivalent Strings
#

# @lc code=start
from typing import List


class Solution:
    def numSpecialEquivGroups(self, words: List[str]) -> int:
        
        unique_groups = set()

        for word in words:
            even_chars = sorted(word[::2])
            odd_chars = sorted(word[1::2])
            signature = (''.join(even_chars), ''.join(odd_chars))
            unique_groups.add(signature)

        return len(unique_groups)
# @lc code=end

