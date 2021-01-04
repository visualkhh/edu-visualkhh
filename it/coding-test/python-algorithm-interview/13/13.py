import math
import sys
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # 숫자 리스트로들어왔을때 변환 list to ListNode
        if isinstance(head, List):
            inHead = head
            head = ListNode(None, None)
            headTemp = head
            for idx in range(len(inHead)-1):
                headTemp.val = inHead[idx]
                headTemp.next = ListNode(inHead[idx+1])
                headTemp = headTemp.next

        items = []
        while isinstance(head, ListNode) and head.val:
            items.append(head.val)
            if head.next:
                head = head.next
            else:
                head = ListNode(None, None)

        headers = items[:len(items) // 2]
        tails = items[math.ceil(len(items) / 2):][::-1]
        if headers == tails:
            return True
        else:
            return False



if __name__ == '__main__':
    palindrome = Solution().isPalindrome(ListNode(1, ListNode(2, ListNode(2, ListNode(1)))))
    # palindrome = Solution().isPalindrome([1,2])
    print('result->', palindrome)
