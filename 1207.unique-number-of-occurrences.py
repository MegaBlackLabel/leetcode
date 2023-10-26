#
# @lc app=leetcode id=1207 lang=python3
#
# [1207] Unique Number of Occurrences
#

# @lc code=start
import collections
from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = collections.Counter(arr)
        occurrences = set()

        for value in count.values():
            if value in occurrences:
                return False
            occurrences.add(value)

        return True
# @lc code=end

