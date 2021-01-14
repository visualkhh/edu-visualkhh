from collections import deque
from typing import List


class MyStack:

    contain = []
    def __init__(self):
        contain = []
        # self.queue = collections.deque() # <-- 디큐로 해도됨
    def push(self, x: int) -> None:
        self.contain.append(x)
    def pop(self) -> int:
        return self.contain.pop()
    def top(self) -> int:
        return len(self.contain) > 0 and self.contain[-1] or False
    def empty(self) -> bool:
        return len(self.contain)<=0 and True or False
if __name__ == '__main__':
    obj = MyStack()
    obj.push(1)
    param_2 = obj.pop()
    param_3 = obj.top()
    param_4 = obj.empty()
    print(param_2, param_2, param_3, param_4)
