import sys
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 맥스값.
        minValue = sys.maxsize
        fit = 0
        for it in prices: #검사.
            minValue = min(minValue, it)
            fit = max(fit, it - minValue)

        return fit


if __name__ == '__main__':
    palindrome = Solution().maxProfit([7, 1, 5, 3, 6, 4])
    print('result->', palindrome)
