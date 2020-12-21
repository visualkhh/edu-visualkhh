# 김테형
import re
from typing import List

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        dig_list = []
        let_list = []

        # Divide digits and letters
        for i in range(len(logs)):
            if logs[i].split()[1].isdigit():
                dig_list.append(logs[i])
            else:
                let_list.append(logs[i])

        # Sort letter list
        let_list.sort(key=lambda x: (x.split()[1:], x.split()[0]))

        return let_list + dig_list
