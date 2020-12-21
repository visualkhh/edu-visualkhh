import re
from typing import List


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        dictionary = self.wordToDictionary(paragraph.lower())
        for it in banned:
            del dictionary[it]
        dictionary = [k for k, v in sorted(dictionary.items(), key=lambda item: item[1], reverse=True)]
        return dictionary[0]

    def wordToDictionary(self, paragraph: str):
        words = re.findall(r'\w+', paragraph)
        dictionary = {}
        for word in words:
            dictionary[word] = dictionary.get(word, 0) + 1
        return dictionary


if __name__ == '__main__':
    palindrome = Solution().mostCommonWord('Bob hit a ball, the hit BALL flew far after it was hit.', ["hit"])
    print(palindrome)
