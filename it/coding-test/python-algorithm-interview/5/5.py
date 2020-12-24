import collections
from typing import List



class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = collections.defaultdict(list)
        for it in strs:
            key = ''.join(sorted(it));
            datas = dictionary.get(key, [])
            datas.append(it)
            dictionary[key] = datas
        return dictionary.values()

if __name__ == '__main__':
    palindrome = Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"])
    # palindrome = Solution().groupAnagrams(["cab","tin","pew","duh","may","ill","buy","bar","max","doc"])
    # palindrome = Solution().groupAnagrams(["duh","ill"])
    print(palindrome)
# [['bar'], ['buy'], ['cab'], ['doc'], ['duh', 'ill'], ['max'], ['may'], ['pew'], ['tin']]
# [["doc"], ["bar"], ["buy"], ["ill"], ["tin"],["cab"],["pew"],["may"],["max"],["duh"]]
