import re
from typing import List

# 민호

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:

        #문자열만을 추출하도록 정규식 활용
        setData = re.sub(r'[^\w]', ' ', paragraph).lower().split()
        words = [word for word in setData if word not in banned]

        #defaultdict로 기본값이 존재하는 딕셔너리 정의
        check = collections.defaultdict(int)
        for word in words:
            check[word] += 1

        #get매서드로 키의 값들을 리턴하고 그중 최대값을 추출
        result = max(check, key = check.get)
        return result
