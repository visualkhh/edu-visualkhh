from collections import deque
from typing import List


class MyQueue:
    contain = []
    def __init__(self):
        contain = []
    def push(self, x: int) -> None:
        self.contain = [x].extend(self.contain)

    def pop(self) -> int:
        return self.contain.pop()

    def peek(self) -> int:
        return self.contain[-1]

    def empty(self) -> bool:
        return not self.contain




# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

if __name__ == '__main__':
    obj = MyQueue()
    obj.push(1)
    param_2 = obj.pop()
    param_3 = obj.top()
    param_4 = obj.empty()
    print(param_2, param_2, param_3, param_4)
