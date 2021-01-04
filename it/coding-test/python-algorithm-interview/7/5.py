from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(nums.__len__()):  # <-- 오 이런 코어 매서드가있네요
            length = len(nums)
            i_ = i + 1
            for j in range(i_, length):
                if nums[i] + nums[j] == target:
                    return [i, j]


if __name__ == '__main__':
    palindrome = Solution().twoSum([2,7,11,15], 9)
    print(palindrome)
