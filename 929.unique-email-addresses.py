#
# @lc app=leetcode id=929 lang=python3
#
# [929] Unique Email Addresses
#

# @lc code=start
from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        seen = set()

        for email in emails:
            local, domain = email.split('@')
            local = local.split('+')[0].replace('.', '')
            seen.add(local + '@' + domain)

        return len(seen)
# @lc code=end

