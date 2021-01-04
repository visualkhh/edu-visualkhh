from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        sort = sorted(nums)
        r = sort[::2]
        return sum(r)


if __name__ == '__main__':
    palindrome = Solution().arrayPairSum([1,4,3,2])
    print('result->', palindrome)

