from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        s.reverse()
if __name__ == '__main__':
    s = ["h", "e", "l", "l", "o"]
    Solution().reverseString(s)
    print(s)