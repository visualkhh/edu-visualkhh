import re
from typing import List

# 김동억
class Solution:
    def sum_raining(self, height_: List[int]) -> int:
        if len(height_) <= 1:
            return 0
        height = height_ + [0]
        direction = 'init'
        high = []
        raining_total = 0
        for idx, cur in enumerate(height[0:-1]):
            next = height[idx + 1]
            if direction is 'init':
                if cur > next:
                    direction = 'low'
                    high.append((idx,cur))
            elif direction is 'high':
                if cur > next and cur >= high[-1][1]:
                    direction = 'low'
                    (prev_idx, prev) = high[-1]
                    threash_hold = cur if prev>cur else prev
                    l = [n if n<threash_hold else threash_hold for n in height[prev_idx+1:idx]]
                    raining_total += (idx - prev_idx - 1 ) * threash_hold - sum(l)
                    high.append((idx,cur))
            elif direction is 'low':
                if cur < next:
                    direction = 'high'
        return raining_total

    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        max_idx = height.index(max(height))
        left_height = height[:max_idx+1]
        right_height = height[max_idx:][::-1]

        left_raining = self.sum_raining(left_height)
        right_raining = self.sum_raining(right_height)

        return left_raining + right_raining
