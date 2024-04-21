#
# @lc app=leetcode id=2129 lang=python3
#
# [2129] Capitalize the Title
#

# @lc code=start
class Solution:
    def capitalizeTitle(self, title: str) -> str:
        return ' '.join(s.lower() if len(s) < 3 else s.capitalize() for s in title.split())
# @lc code=end

