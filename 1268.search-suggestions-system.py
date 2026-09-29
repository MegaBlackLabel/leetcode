#
# @lc app=leetcode id=1268 lang=python3
#
# [1268] Search Suggestions System
#

# @lc code=start
from typing import List, Optional

class Trie:
    def __init__(self):
        self.children: List[Optional['Trie']] = [None] * 26
        self.product_indices: List[int] = []

    def insert(self, word: str, product_index: int) -> None:
        """Insert a word into the trie with its product index."""
        current_node = self

        for char in word:
            char_index = ord(char) - ord('a')

            if current_node.children[char_index] is None:
                current_node.children[char_index] = Trie()

            current_node = current_node.children[char_index]

            if len(current_node.product_indices) < 3:
                current_node.product_indices.append(product_index)

    def search(self, word: str) -> List[List[int]]:
        """Search for product suggestions for each prefix of the given word."""
        current_node = self
        suggestions = [[] for _ in range(len(word))]

        for position, char in enumerate(word):
            char_index = ord(char) - ord('a')

            if current_node.children[char_index] is None:
                break

            current_node = current_node.children[char_index]
            suggestions[position] = current_node.product_indices

        return suggestions

class Solution:
    def suggestedProducts(self, products: list[str], searchWord: str) -> list[list[str]]:
        products.sort()

        trie = Trie()
        for index, product in enumerate(products):
            trie.insert(product, index)

        suggestion_indices = trie.search(searchWord)
        return [[products[index] for index in indices] for indices in suggestion_indices]
# @lc code=end

