# 민호
import re
from typing import List

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:

        digitLogs = []
        letterLogs = []

        for log in logs:
            setData = log.split()[1] #첫번째 문자열을 판정기준으로 사용
            digitLogs.append(log) if setData.isdigit() else letterLogs.append(log)

        """
        sort의 정렬기준 인자 key는 하나의 인자를 받고
        정렬기준이 되는 키를 리턴하는 함수가 되어야
        키에 전달되는 람다함수는 다음과 동일 
        def sample(x):
            return x.split()[1],x.split()[0])
        여기서 리턴 받은 값은 첫번째인자 확인후 동일한 경우 식별자를 확인하게함
        """
        letterLogs.sort(key=lambda x: (x.split()[1:],x.split()[0]))

        return letterLogs + digitLogs
