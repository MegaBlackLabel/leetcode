#
# @lc app=leetcode id=1528 lang=python3
#
# [1528] Shuffle String
#

# @lc code=start
from typing import List


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res = [''] * len(s)
      
        # Loop through each character and its intended index
        for index, character in enumerate(s):
            target = indices[index]
            # Place the character in the correct index of the restored string
            res[target] = character
      
        # Join all characters to form the restored string and return it
        return ''.join(res)
# @lc code=end

