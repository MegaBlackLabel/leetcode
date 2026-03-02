#
# @lc app=leetcode id=3083 lang=python3
#
# [3083] Existence of a Substring in a String and Its Reverse
#

# @lc code=start
class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        reversed_s = s[::-1]
        for i in range(len(s) - 1):
            sub = s[i:i+2]  # Get the current 2-character substring
            if sub in reversed_s:  # Check if the substring is in the reversed string
                return True
        return False

# @lc code=end

