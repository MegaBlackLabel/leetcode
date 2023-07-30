#
# @lc app=leetcode id=728 lang=python3
#
# [728] Self Dividing Numbers
#

# @lc code=start
from typing import List


class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        return [num for num in range(left, right + 1) if all(n != 0 and num % n == 0 for n in map(int, str(num)))]
# @lc code=end

