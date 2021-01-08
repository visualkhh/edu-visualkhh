import math
import sys
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:

        cur = self.listNodeToList(head)
        stay = sorted(list(filter(lambda x: cur[0] <= x, cur)))
        stay.extend(sorted(list(filter(lambda x: cur[0] > x, cur))))
        stay_ = stay[0] % 2
        last = sorted(list(filter(lambda x: x%2 == stay_, cur)))
        last.extend(sorted(list(filter(lambda x: x%2 != stay_, cur))))
        for i in last:
            print(i)

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
    # l1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))
    l1 = ListNode(2, ListNode(1, ListNode(3, ListNode(5, ListNode(6, ListNode(4, ListNode(7)))))))
    data = Solution().oddEvenList(l1)
    print('result->', data)
