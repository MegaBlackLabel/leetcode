#
# @lc app=leetcode id=721 lang=python3
#
# [721] Accounts Merge
#

# @lc code=start
from typing import List
from collections import defaultdict

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
    

        parent = {}
        email_to_name = {}

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            parent[find(x)] = find(y)

        for account in accounts:
            name = account[0]
            first_email = account[1]
            for email in account[1:]:
                if email not in parent:
                    parent[email] = email
                email_to_name[email] = name
                union(first_email, email)

        merged_accounts = defaultdict(set)
        for email in parent:
            root = find(email)
            merged_accounts[root].add(email)

        result = []
        for root, emails in merged_accounts.items():
            result.append([email_to_name[root]] + sorted(emails))

        return result
# @lc code=end

