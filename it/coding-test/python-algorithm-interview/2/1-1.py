# 김동억
from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        chkIndex = len(s) // 2  # check index
        for i in range(chkIndex):
            s[-i - 1], s[i] = s[i], s[-i - 1]  # swap


# x = 3
# y = 5
# print("x :%d y : %d" % (x,y))
# x, y = y, x
# print("x :%d y : %d" % (x,y))
