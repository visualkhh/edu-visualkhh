import math
import sys
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1s = self.listNodeToList(l1)
        l2s = self.listNodeToList(l2)
        #평탄화
        self.flat(l1s, l2s);
        i = 0
        while True:
            s = l1s[i] + l2s[i]
            up = int(round(s / 10, 1))
            # print(upzz, up)
            stay = int(((s / 10)  * 10 )) - (up*10)
            l1s[i] = stay
            i += 1
            if(up > 0 and len(l1s) == i):
                l1s.append(up)
                self.flat(l1s,l2s)
            elif(up > 0):
                l1s[i] += up

            if(len(l1s) == i):
                break
        return l1s

    def flat(self, l1s: List, l2s: List):
        #평탄화
        for i in range(len(l1s) - len(l2s)):
            l2s.append(0)

        for i in range(len(l2s) - len(l1s)):
            l1s.append(0)

    def listNodeToList(self, head: List or ListNode) -> List:
        items = []
        while isinstance(head, ListNode) and head and head.val:
            items.append(head.val)
            if head.next:
                head = head.next
            else:
                head = ListNode(None, None)
        return items

if __name__ == '__main__':
    l1 = ListNode(2, ListNode(4, ListNode(3)))
    l2 = ListNode(5, ListNode(6, ListNode(4)))
    data = Solution().addTwoNumbers(l1, l2)
    print('result->', data)
