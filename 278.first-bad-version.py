#
# @lc app=leetcode id=278 lang=python3
#
# [278] First Bad Version
#

# @lc code=start
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:


class Solution:
    def firstBadVersion(self, n: int) -> int:
        if n == 1:
            return 1
        begin = 1
        end = n
        while begin < end:
            mid = begin + (end - begin) / 2
            if isBadVersion(mid):
                end = mid
            else:
                begin = mid + 1
        return int(begin)


# @lc code=end
