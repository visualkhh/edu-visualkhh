# 민호
from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        pnt = s.__len__()
        for i in range(0, pnt // 2):
            pnt -= 1
            s[i], s[pnt] = s[pnt], s[i]
if __name__ == '__main__':
    s = ["h", "e", "l", "l", "o"]
    Solution().reverseString(s)
    print(s)