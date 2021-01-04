from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:

        sum = 0

        if len(height)<2:
            return sum
        #평탄화
        maxVal = max(height)
        maxIdx = height.index(maxVal)
        watnMax = max(height[:maxIdx] + height[maxIdx+1:])
        print(maxVal, watnMax)
        height = list(map(lambda x: x >= maxVal and watnMax or x, height))
        print(height)


        for idx, val in enumerate(height):
            print(idx, val)
            for sidx, sVal in enumerate(height):
                print(sidx, sVal)


        return 1


if __name__ == '__main__':
    palindrome = Solution().trap([5, 4, 1, 2])
    # palindrome = Solution().trap([2,1,0,2])
    # palindrome = Solution().trap([2,1,0,2,3])
    # palindrome = Solution().trap([4,2,0,3,2,5])
    # palindrome = Solution().trap([3, 2, 1, 2, 1])
    # palindrome = Solution().trap([0, 1, 0, 2, 1, 0, 1, 3])
    # palindrome = Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
    # palindrome = Solution().trap([4, 2, 3])
    # palindrome = Solution().trap([0, 1, 0, 2])
    print('result->', palindrome)

