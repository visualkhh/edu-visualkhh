# 김동억
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx1, n1 in enumerate(nums[:-1]):
            for idx2, n2 in enumerate(nums[idx1+1:]):
                if n1+n2 == target:
                    return [idx1,idx1+idx2+1]
        return None
