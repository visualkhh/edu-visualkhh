# 주연경
import re
from typing import List

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:

        # digit_logs = [s for s in logs if s.split()[1].isdigit()]
        # str_logs = [s for s in logs if s.split()[1].isalpha()]

        digit_logs = []
        str_logs = []
        for s in logs:
            if s.split()[1].isdigit():
                digit_logs.append(s)
            else:
                str_logs.append(s)

        return sorted(str_logs, key=lambda x: (x.split()[1:], x.split()[0])) + digit_logs
