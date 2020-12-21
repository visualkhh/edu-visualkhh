# 김동억
import re
from typing import List

class Solution:

    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        grp = {}
        letList = []
        digList = []
        for log in logs:
            isNumber = True
            cList = log.split()
            for c in cList[1:]:
                if(c.isalpha()):
                    isNumber = False
                    break

            if isNumber:
                digList.append((log, cList[1:]))
            else:
                letList.append((log, cList[1:]))

        sortedList = sorted(letList, key=lambda l: (l[1],l[0])) + digList
        return map(lambda l: l[0], sortedList)
