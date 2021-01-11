from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        re = []
        scope = {')': '(','>': '<','}': '{',']': '[',}
        for d in s:
            if d not in scope:
                re.append(d)
            elif not re or scope[d] != re.pop():
                return False
        return len(re) == 0


if __name__ == '__main__':
    data = Solution().isValid("()")
    print('result->', data)
