from typing import List

#주연경
class Solution:
    def trap(self, height: List[int]) -> int:


        if len(height) == 0 :
            return 0

        result = 0
        left, right = 0, len(height)-1
        max_left, max_right = height[left], height[right]

        while left < right :
            max_left = max(height[left], max_left)
            max_right = max(height[right], max_right)

            result += max_left - height[left]
            result += max_right - height[right]

            if max_left == max(height) :
                right -= 1
            elif max_right == max(height) :
                left += 1
            else :
                left += 1
                right -= 1

        return result
