from typing import List



class Solution:
    def trap(self, height: List[int]) -> int:

        start = {'use': False, 'idx': 0, 'value': 0}
        # start = False
        end = False

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

        for idx in range(len(height) - 1):
            it = height[idx]
            next = height[idx + 1]
            # print('-> ', height[idx+1:], self.isGrateThanEqual(it, height[idx+1:]))
            # continue
            nexList = height[idx+1:]
            if it > next and start['use'] == False and self.isGrateThanEqual(it, nexList):
                start['use'] = True
                start['idx'] = idx
                start['value'] = it

            if start['use'] == True and start['value'] <= next:
                start['use'] = False
                start['idx'] = idx
                start['value'] = 0

            if start['use']:
                value_next = start['value'] - next
                print('=-->', value_next)
                if value_next > 0:
                    sum += start['value'] - next

            print(it, next)

        # print(sum);
        return sum

    def isGrateThanEqual(self, it: int, datas: List[int]) -> bool:
        l = list(filter(lambda x: x >= it, datas))
        return len(l) > 0


if __name__ == '__main__':
    palindrome = Solution().trap([5,4,1,2])
    # palindrome = Solution().trap([2,1,0,2])
    # palindrome = Solution().trap([2,1,0,2,3])
    # palindrome = Solution().trap([4,2,0,3,2,5])
    # palindrome = Solution().trap([3, 2, 1, 2, 1])
    # palindrome = Solution().trap([0, 1, 0, 2, 1, 0, 1, 3])
    # palindrome = Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
    # palindrome = Solution().trap([4, 2, 3])
    # palindrome = Solution().trap([0, 1, 0, 2])
    print('result->', palindrome)
