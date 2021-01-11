# 주연경
class Solution:
    def isValid(self, s: str) -> bool:

        s = list(s)

        open = ["(", "[", "{"]
        close = [")", "]", "}"]
        stack = []
        result = True
        length = len(s)

        if length % 2 != 0:
            result = False
        else:
            for _ in range(length):
                c = s.pop()
                if c in close:
                    stack.append(c)
                else:
                    if not stack:
                        result = False
                        break
                    elif stack and open.index(c) != close.index(stack.pop()):
                        result = False
                        break

        if stack:
            result = False

        return result
