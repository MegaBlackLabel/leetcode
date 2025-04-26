#
# @lc app=leetcode id=433 lang=python3
#
# [433] Minimum Genetic Mutation
#

# @lc code=start
from collections import deque
from typing import List


class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        
        if endGene not in bank:
            return -1

        queue = deque([startGene])
        visited = set([startGene])
        mutations = 0

        while queue:
            for _ in range(len(queue)):
                gene = queue.popleft()
                if gene == endGene:
                    return mutations

                for i in range(len(gene)):
                    for c in "ACGT":
                        new_gene = gene[:i] + c + gene[i+1:]
                        if new_gene in bank and new_gene not in visited:
                            visited.add(new_gene)
                            queue.append(new_gene)

            mutations += 1

        return -1
# @lc code=end

