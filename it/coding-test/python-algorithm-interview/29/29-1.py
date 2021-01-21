import collections


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:

        counterDict = collections.Counter(stones)
        result = 0

        for _, ch in enumerate(jewels):
            if ch in counterDict.keys():
                result += counterDict[ch]

        return result


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
