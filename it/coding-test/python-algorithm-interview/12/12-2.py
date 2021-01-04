import sys
from typing import List

#주연경
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if len(prices) <= 1:
            return 0

        answer = 0
        min_price, max_price = prices[0], prices[0]
        for price in prices:
            if price < min_price:
                min_price, max_price = price, price
            if price > max_price:
                max_price = price

            if max_price - min_price > answer:
                answer = max_price - min_price

        return answer
