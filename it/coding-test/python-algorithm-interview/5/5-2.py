import collections
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # anagrams = collections.defaultdict(list)
        anagrams = {}
        # print('---?', anagrams)
        for word in strs:
            # 정렬하여 딕셔너리에 추가
            # at = anagrams[''.join(sorted(word))]
            # anagrams['1'] = 'zz'
            # print('---?', anagrams, anagrams['1'])
            join = ''.join(sorted(word))
            atList = anagrams.get(join, [])
            atList.append(word)
            anagrams[join] = atList;
            # if join in anagrams:
            #     anagrams[join].append(word)
            # else:
            #     anagrams[join] = [word]
        # return list(anagrams.values())
        #     print(anagrams.get(join))
            # anagrams.get(''.join(sorted(word)), []).append(word)
            # at.append(word) if anagrams.has else anagrams[''.join(sorted(word))] = [word]
            # anagrams[''.join(sorted(word))].append(word)
            # print('---',word, sorted(word).join(''));
            # anagrams[sorted(word)].append(word)
        return list(anagrams.values())

if __name__ == '__main__':
    palindrome = Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"])
    print(palindrome)
