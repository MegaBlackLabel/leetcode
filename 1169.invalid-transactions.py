#
# @lc app=leetcode id=1169 lang=python3
#
# [1169] Invalid Transactions
#

# @lc code=start
from collections import defaultdict


class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        transactions_by_name = defaultdict(list)
      
        invalid_indices = set()
      
        for index, transaction_str in enumerate(transactions):
            name, time_str, amount_str, city = transaction_str.split(",")
            time = int(time_str)
            amount = int(amount_str)
          
            transactions_by_name[name].append((time, city, index))
          
            if amount > 1000:
                invalid_indices.add(index)
          
            for prev_time, prev_city, prev_index in transactions_by_name[name]:
                if prev_city != city and abs(time - prev_time) <= 60:
                    invalid_indices.add(index)
                    invalid_indices.add(prev_index)
      
        return [transactions[i] for i in invalid_indices]
# @lc code=end

