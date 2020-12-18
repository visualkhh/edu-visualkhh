# 주연경
from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        length = len(s)
        mid = length // 2
        for i, c in enumerate(s) :

            if i >= mid :
                break
            tmp = s[i]
            s[i] = s[length-1-i]
            s[length - 1 - i] = tm
