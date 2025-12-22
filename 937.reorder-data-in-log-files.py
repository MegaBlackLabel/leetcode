#
# @lc app=leetcode id=937 lang=python3
#
# [937] Reorder Data in Log Files
#

# @lc code=start
from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        
        def get_key(log: str):
            id_, rest = log.split(" ", 1)
            is_digit = rest[0].isdigit()
            return (1, ) if is_digit else (0, rest, id_)

        return sorted(logs, key=get_key)
# @lc code=end

