#
# @lc app=leetcode id=898 lang=python3
#
# [898] Bitwise ORs of Subarrays
#

# @lc code=start
from typing import List


class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        
        result = set()
        current = set()

        for num in arr:
            current = {num | prev for prev in current} | {num}
            result |= current

        return len(result)
# @lc code=end

