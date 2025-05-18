#
# @lc app=leetcode id=468 lang=python3
#
# [468] Validate IP Address
#

# @lc code=start
class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        
        def isIPv4(ip: str) -> bool:
            parts = ip.split('.')
            if len(parts) != 4:
                return False
            for part in parts:
                if not part.isdigit() or not 0 <= int(part) <= 255 or (part[0] == '0' and len(part) > 1):
                    return False
            return True

        def isIPv6(ip: str) -> bool:
            parts = ip.split(':')
            if len(parts) != 8:
                return False
            for part in parts:
                if not (1 <= len(part) <= 4) or not all(c in '0123456789abcdefABCDEF' for c in part):
                    return False
            return True

        if queryIP.count('.') == 3 and isIPv4(queryIP):
            return "IPv4"
        elif queryIP.count(':') == 7 and isIPv6(queryIP):
            return "IPv6"
        else:
            return "Neither"
# @lc code=end

