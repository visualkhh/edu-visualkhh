import re
from typing import List

# 주연경

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:

        re_paragraph = re.sub('[!?\',;.]', ' ', paragraph).lower()
        words = [word for word in re_paragraph.split() if word not in banned]

        counts = dict()
        for word in words :
            if word in counts.keys() :
                counts[word] += 1
            else :
                counts[word] = 1

        return max(counts, key = lambda x : counts.get(x))

        '''
        counter = collections.Counter(arr)
        
        for c in counter.most_common(len(counter)) :
            if c[0] not in banned :
                return c[0]
        '''


