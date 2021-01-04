from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        returns = []
        point = 1
        r1 = range(0, len(nums))
        for idx in r1:
            returns.append(point)
            point = point * nums[idx]

        point = 1
        r2 = range(len(nums) - 1, 0 - 1, -1) #뒤로 한칸씩.
        for idx in r2:
            returns[idx] = returns[idx] * point
            point = point * nums[idx]
        return returns


if __name__ == '__main__':
    palindrome = Solution().productExceptSelf([1, 2, 3, 4])
    print('result->', palindrome)
