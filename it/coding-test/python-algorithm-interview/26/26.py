from collections import deque


class MyCircularDeque:

    def __init__(self, k: int):
        self.q = deque(maxlen=k)
        self.max = k
    def insertFront(self, value: int) -> bool:
        self.q.appendleft(value)
        return True
    def insertLast(self, value: int) -> bool:
        self.q.append(value)
    def deleteFront(self) -> bool:
        self.q.popleft()
        return True
    def deleteLast(self) -> bool:
        self.q.pop()
        return True;
    def getFront(self) -> int:
        return self.q.index(0)
    def getRear(self) -> int:
        if self.isEmpty():
            return -1;
        else:
            return self.q.index(len(self.q))
    def isEmpty(self) -> bool:
        if len(self.q) <= 0:
            return True
        else:
            return False
    def isFull(self) -> bool:
        if len(self.q) >= self.max:
            return True
        else:
            return False


if __name__ == '__main__':
    obj = MyCircularDeque(5)
    param_1 = obj.insertFront(1)
    param_2 = obj.insertLast(4)
    param_3 = obj.deleteFront()
    param_4 = obj.deleteLast()
    param_5 = obj.getFront()
    param_6 = obj.getRear()
    param_7 = obj.isEmpty()
    param_8 = obj.isFull()
    print(param_2, param_2, param_3, param_4)

# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
