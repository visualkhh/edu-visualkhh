import re
from typing import List

# 김태형

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        new_words = []
        cnt = []

        words = paragraph.lower()
        words = re.sub('[^a-z0-9]', ' ', words)
        words = words.split()

        for word in words:
            if word not in banned:
                new_words.append(word)

        for word in new_words:
            cnt.append(new_words.count(word))

        idx = cnt.index(max(cnt))

        return (new_words[idx])
