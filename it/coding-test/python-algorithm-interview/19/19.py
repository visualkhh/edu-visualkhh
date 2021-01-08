import math
import sys
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        cur = self.listNodeToList(head)
        head = []
        body = []
        tail = []

        startIdx = 0
        for i, d in enumerate(cur):
            if d >= m:
                startIdx = i
                break
            else:
                head.append(d)

        endIdx = startIdx
        for i, d in enumerate(cur):
            if i >= startIdx and d >= m and d <= n:
                body.append(d)
                endIdx = i

        for i, d in enumerate(cur):
            if i > endIdx:
                tail.append(d)

        head.extend(list(sorted(body, reverse=True)))
        head.extend(tail)
        print(head)


    def listNodeToList(self, head: List or ListNode) -> List:
        items = []
        while isinstance(head, ListNode) and head and head.val:
            items.append(head.val)
            if head.next:
                head = head.next
            else:
                head = ListNode(None, None)
        return items

    def listToListNode(self, head: List or ListNode) -> ListNode:
        if isinstance(head, List):
            inHead = head
            head = ListNode(None, None)
            headTemp = head
            for idx in range(len(inHead)-1):
                headTemp.val = inHead[idx]
                headTemp.next = ListNode(inHead[idx+1])
                headTemp = headTemp.next
        return head

if __name__ == '__main__':
    l1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(None))))))
    data = Solution().reverseBetween(l1, 2, 4)
    print('result->', data)
