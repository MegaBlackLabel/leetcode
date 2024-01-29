#
# @lc app=leetcode id=1700 lang=python3
#
# [1700] Number of Students Unable to Eat Lunch
#

# @lc code=start
import collections
from typing import List


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count = collections.Counter(students)

        for i, sandwich in enumerate(sandwiches):
            if count[sandwich] == 0:
                return len(sandwiches) - i
            count[sandwich] -= 1

        return 0
# @lc code=end

