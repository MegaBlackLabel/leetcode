#
# @lc app=leetcode id=1342 lang=python3
#
# [1342] Number of Steps to Reduce a Number to Zero
#

# @lc code=start
class Solution:
    def numberOfSteps(self, num: int) -> int:
        if num == 0:
            return 0
        
        subtractSteps = num.bit_count()
        divideSteps = num.bit_length() - 1

        return subtractSteps + divideSteps
# @lc code=end

