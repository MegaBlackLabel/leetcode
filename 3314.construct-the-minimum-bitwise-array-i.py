#
# @lc app=leetcode id=3314 lang=python3
#
# [3314] Construct the Minimum Bitwise Array I
#

# @lc code=start
from typing import List


class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []
        for n in nums:
            found = False
            # 最小のxを探すため0から順に試す
            for x in range(n):
                if (x | (x + 1)) == n:
                    ans.append(x)
                    found = True
                    break
            if not found:
                ans.append(-1)
        return ans
# @lc code=end

