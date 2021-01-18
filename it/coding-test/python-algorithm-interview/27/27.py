import math
import sys
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        re = []
        for it in lists:
            re += (self.listNodeToList(it))
        return sorted(re)


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
    l1 = ListNode(1, ListNode(4, ListNode(5)))
    l2 = ListNode(1, ListNode(3, ListNode(4)))
    l3 = ListNode(2, ListNode(6))
    data = Solution().mergeKLists([l1, l2, l3])
    print('result->', data)
