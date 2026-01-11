#
# @lc app=leetcode id=966 lang=python3
#
# [966] Vowel Spellchecker
#

# @lc code=start
from typing import List


class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        exact_words = set(wordlist)
        case_insensitive_map = {}
        vowel_error_map = {}

        def devowel(word: str) -> str:
            return ''.join('*' if c in 'aeiou' else c for c in word.lower())

        for word in wordlist:
            lower_word = word.lower()
            if lower_word not in case_insensitive_map:
                case_insensitive_map[lower_word] = word
            devoweled_word = devowel(word)
            if devoweled_word not in vowel_error_map:
                vowel_error_map[devoweled_word] = word

        result = []
        for query in queries:
            if query in exact_words:
                result.append(query)
            else:
                lower_query = query.lower()
                if lower_query in case_insensitive_map:
                    result.append(case_insensitive_map[lower_query])
                else:
                    devoweled_query = devowel(query)
                    if devoweled_query in vowel_error_map:
                        result.append(vowel_error_map[devoweled_query])
                    else:
                        result.append("")

        return result
# @lc code=end

