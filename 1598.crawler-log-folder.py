#
# @lc app=leetcode id=1598 lang=python3
#
# [1598] Crawler Log Folder
#

# @lc code=start
from typing import List


class Solution:
    def minOperations(self, logs: List[str]) -> int:
        ans = 0
      
        for operation in logs:
            if operation == "../":
                ans = max(0, ans - 1)
            elif operation != "./":
                ans += 1
      
        return ans
# @lc code=end

