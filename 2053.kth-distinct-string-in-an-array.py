#
# @lc app=leetcode id=2053 lang=python3
#
# [2053] Kth Distinct String in an Array
#

# @lc code=start
import collections
from typing import List


class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count = collections.Counter(arr)

        for a in arr:
            if count[a] == 1:
                k -= 1
                if k == 0:
                    return a

        return ''
# @lc code=end

