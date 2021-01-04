# 김태형
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx_1 in range(len(nums)):
            for idx_2 in range(len(nums)):
                if idx_1 == idx_2:
                    continue
                else:
                    if nums[idx_1] + nums[idx_2] == target:
                        return [idx_1, idx_2]
