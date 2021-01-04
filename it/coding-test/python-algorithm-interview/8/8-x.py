from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:

        # maxVal = max(height)
        # maxIdx = height.index(max(height))
        #
        # head = height[:maxIdx][::-1]
        # head.insert(0, maxVal)
        # targetList = [head, height[maxIdx:]]
        # # print(targetList)
        #
        # for group in targetList:
        #     print(group)
        #     for it in group:
        #         print(it, end=' ')
        #     print()

        start = {'use': False, 'idx': 0, 'value': 0}
        end = False

        sum = 0

        for idx, it in enumerate(height):
            than = self.isGrateThan(it, height[:idx])

            start['use'] = start['use'] == False and than == True
            if start['use']:
                start['idx'] = idx
                start['value'] = it
                sum += 1

            print(it, than, start, end = '\n\n')


        # append = height[:maxIdx].insert(0, maxVal)
        # print(append)
        # print(maxIdx)
        # print(height[:maxIdx])
        # print(height[:maxIdx][::-1])
        # print(height[maxIdx:])
        # print(height[:maxIdx][::-1])
        return 1

    def isGrateThan(self, it: int, datas: List[int]) -> bool:
        l = list(filter(lambda x: x > it, datas))
        print(l)
        return len(l) > 0


if __name__ == '__main__':
    palindrome = Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
    print('result->', palindrome)
