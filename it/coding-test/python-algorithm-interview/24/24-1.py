class MyQueue:

    def __init__(self):
        self.list = []


    def push(self, x: int) -> None:
        self.list = [x] + self.list


    def pop(self) -> int:
        return self.list.pop()


    def peek(self) -> int:
        return self.list[-1]


    def empty(self) -> bool:
        return not self.list



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
