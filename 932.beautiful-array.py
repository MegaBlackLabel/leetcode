#
# @lc app=leetcode id=932 lang=python3
#
# [932] Beautiful Array
#

# @lc code=start
from typing import List


class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        
        result = [1]

        while len(result) < n:
            result = [x * 2 - 1 for x in result] + [x * 2 for x in result]

        return [x for x in result if x <= n]
# @lc code=end

