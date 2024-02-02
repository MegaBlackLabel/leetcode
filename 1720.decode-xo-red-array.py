#
# @lc app=leetcode id=1720 lang=python3
#
# [1720] Decode XORed Array
#

# @lc code=start
from typing import List


class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        ans = [first]

        for e in encoded:
            ans.append(e ^ ans[-1])

        return ans
# @lc code=end

