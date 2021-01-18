class ListNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class MyCircularDeque:

    def __init__(self, k: int):
        self.head, self.tail = ListNode(None), ListNode(None)
        self.size = k
        self.len = 0

        self.head.right = self.tail
        self.tail.left = self.head


    def insertFront(self, value: int) -> bool:
        if self.len == self.size:
            return False

        right = self.head.right
        node = ListNode(value)
        self.head.right = node
        node.left, node.right = self.head, right
        right.left = node

        self.len += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.len == self.size:
            return False

        left = self.tail.left
        node = ListNode(value)
        self.tail.left = node
        node.left, node.right = left, self.tail
        left.right = node

        self.len += 1
        return True

    def deleteFront(self) -> bool:
        if self.len == 0:
            return False

        node = self.head.right
        self.head.right = node.right
        node.right.left = self.head

        self.len -= 1
        return True

    def deleteLast(self) -> bool:
        if self.len == 0:
            return False

        node = self.tail.left
        self.tail.left = node.left
        node.left.right = self.tail

        self.len -= 1
        return True

    def getFront(self) -> int:
        if self.len == 0:
            return -1
        return self.head.right.val


    def getRear(self) -> int:
        if self.len == 0:
            return -1
        return self.tail.left.val


    def isEmpty(self) -> bool:
        return self.len == 0


    def isFull(self) -> bool:
        return self.len == self.size


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
