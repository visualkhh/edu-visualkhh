# 주연경
from typing import List

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:

        nums = sorted(nums)
        return sum([nums[i] for i in range(len(nums)) if i % 2 == 0])
