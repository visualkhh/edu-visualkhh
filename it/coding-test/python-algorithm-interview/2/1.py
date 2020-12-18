# 현하
from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        length = len(s)
        for idx in range(length//2):
            targetIndex = length - idx - 1
            temp = s[idx]
            s[idx] = s[targetIndex]
            s[targetIndex] = temp
        # print(''.join(s))


if __name__ == '__main__':
    Solution().reverseString([char for char in "show me the money"])
