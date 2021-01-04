from typing import List

#김동억
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        left_result = []
        left_result.append(1)
        for idx in range(0, length-1): # start stop(not include) step
            left_result.append(left_result[idx] * nums[idx])

        right_result = []
        right_result.append(1)
        for idx in range(0,length-1):
            right_result.append(right_result[idx] * nums[length-idx-1])

        return [left_result[idx]* right_result[length-idx-1] for idx in range(length)]
