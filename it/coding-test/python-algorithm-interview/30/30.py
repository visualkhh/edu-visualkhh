class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = dict()
        for _, ch in enumerate(s):
            d[ch] = ch
        return len(d)

if __name__ == '__main__':
    obj = Solution().lengthOfLongestSubstring('abcabcbb')
    print(obj)



# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
