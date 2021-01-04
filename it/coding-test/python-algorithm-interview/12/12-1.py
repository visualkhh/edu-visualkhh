import sys
from typing import List

#김동억
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min = sys.maxsize
        for n in prices:
            min = n if n < min else min
            profit = n-min if n-min > profit else profit
        return profit
