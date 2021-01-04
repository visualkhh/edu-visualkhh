# 민호

from typing import List

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        item = sorted(nums)[::2]
        result = sum(item)
        return result
