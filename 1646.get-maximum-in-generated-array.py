#
# @lc app=leetcode id=1646 lang=python3
#
# [1646] Get Maximum in Generated Array
#

# @lc code=start
class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1

        nums = [0] * (n + 1)
        nums[1] = 1

        i = 1
        while 2 * i + 1 <= n:
            nums[2 * i] = nums[i]
            nums[2 * i + 1] = nums[i] + nums[i + 1]
            i += 1

        return max(nums)
# @lc code=end

