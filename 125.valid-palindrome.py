#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        sLower = s.lower()

        sAlphaNum = ""
        for ch in sLower:
            if ch.isalnum():
                sAlphaNum += ch

        print(sAlphaNum)

        startPtr, endPtr = 0, len(sAlphaNum) - 1
        while endPtr > startPtr:
            # Return early as soon as a non-match is detected
            if sAlphaNum[startPtr] != sAlphaNum[endPtr]:
                return False

            startPtr += 1
            endPtr -= 1

        return True


# @lc code=end
