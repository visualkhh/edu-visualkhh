from collections import deque
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        r = ''
        for i in s:
            if r.find(i) == -1:
                r+=i
        return ''.join(sorted(r))

if __name__ == '__main__':
    data = Solution().removeDuplicateLetters("cbacdcbc")
    print('result->', data)
