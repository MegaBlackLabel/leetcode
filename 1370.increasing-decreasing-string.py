#
# @lc app=leetcode id=1370 lang=python3
#
# [1370] Increasing Decreasing String
#

# @lc code=start
import collections
import string


class Solution:
    def sortString(self, s: str) -> str:
        ans = []
        count = collections.Counter(s)

        while count:
            for chars in string.ascii_lowercase, reversed(string.ascii_lowercase):
                ans += [c for c in chars if c in count]
                count -= dict.fromkeys(count, 1)

        return ''.join(ans)

# @lc code=end

