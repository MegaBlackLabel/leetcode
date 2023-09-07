#
# @lc app=leetcode id=914 lang=python3
#
# [914] X of a Kind in a Deck of Cards
#

# @lc code=start
import collections
import functools
import math
from typing import List


class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        count = collections.Counter(deck)
        return functools.reduce(math.gcd, count.values()) >= 2
# @lc code=end

