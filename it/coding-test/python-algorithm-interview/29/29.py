class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        cnt = 0
        for it in jewels:
            cnt += stones.count(it)
        return cnt


if __name__ == '__main__':
    obj = Solution().numJewelsInStones(jewels = 'aAz', stones = 'aAAbbbb')
    print(obj)



# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
