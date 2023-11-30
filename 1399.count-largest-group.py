#
# @lc app=leetcode id=1399 lang=python3
#
# [1399] Count Largest Group
#

# @lc code=start
class Solution:
    def countLargestGroup(self, n: int) -> int:
        count = [0] * (9 * 4 + 1)
        
        for i in range(1, n + 1):
            count[self._getDigitSum(i)] += 1
        return count.count(max(count))

    def _getDigitSum(self, num: int) -> int:
        digitSum = 0
        
        while num > 0:
            digitSum += num % 10
            num //= 10
        
        return digitSum
# @lc code=end

