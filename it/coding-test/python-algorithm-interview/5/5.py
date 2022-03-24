from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        rtn = []
        for idx, it in enumerate(strs):
            for sidx, sit in enumerate(strs):
                if (idx != sidx and sorted(it) == sorted(sit)):
                    rtn[idx].append(sit)
        return rtn;

if __name__ == '__main__':
    s = Solution()
    print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    # print(s.groupAnagrams([""]))