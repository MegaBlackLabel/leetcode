#
# @lc app=leetcode id=811 lang=python3
#
# [811] Subdomain Visit Count
#

# @lc code=start
from typing import List


class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        
        count = {}
        for cpdomain in cpdomains:
            n, domain = cpdomain.split()
            n = int(n)
            fragments = domain.split('.')
            for i in range(len(fragments)):
                subdomain = '.'.join(fragments[i:])
                count[subdomain] = count.get(subdomain, 0) + n
        return [f"{n} {domain}" for domain, n in count.items()]
# @lc code=end

