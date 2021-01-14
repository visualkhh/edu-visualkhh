from collections import deque
from typing import List


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        # 빈방 생성.
        re = [0] * len(T)
        temp = []
        for i, cur in enumerate(T):
            while temp and cur > T[temp[-1]]:
                last = temp.pop()
                re[last] = i - last
            temp.append(i)

        return re



if __name__ == '__main__':
    data = Solution().dailyTemperatures( [73, 74, 75, 71, 69, 72, 76, 73])
    print('result->', data)
