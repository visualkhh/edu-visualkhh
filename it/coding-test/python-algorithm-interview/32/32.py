import collections
import re
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # r = 0
        # for it in grid:
        #     strGrid = ''.join(it)
        #     print(strGrid)
        #     if re.match('^11110$', strGrid) and re.match('11110$', strGrid):
        #         r+=1
        #         print('--', strGrid)
        #     # print(strGrid, match)
        # return r;
        def dfs(i, j):
            # 더 이상 땅이 아닌 경우 종료
            if i < 0 or i >= len(grid) or \
                    j < 0 or j >= len(grid[0]) or \
                    grid[i][j] != '1':
                return

            grid[i][j] = 0

            # 동서남북 탐색
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(i, j)
                    print(i,j)

                    # 모든 육지 탐색 후 카운트 1 증가
                    count += 1
        return count

if __name__ == '__main__':
    grid = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]
    obj = Solution().numIslands(grid)
    print(obj)



# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
