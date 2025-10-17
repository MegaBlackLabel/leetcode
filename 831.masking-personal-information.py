#
# @lc app=leetcode id=831 lang=python3
#
# [831] Masking Personal Information
#

# @lc code=start
class Solution:
    def maskPII(self, s: str) -> str:
        
        if "@" in s:
            name, domain = s.lower().split("@")
            return f"{name[0]}*****{name[-1]}@{domain}"
        else:
            digits = [c for c in s if c.isdigit()]
            local = "***-***-" + "".join(digits[-4:])
            if len(digits) == 10:
                return local
            else:
                return "+" + "*" * (len(digits) - 10) + "-" + local
# @lc code=end

