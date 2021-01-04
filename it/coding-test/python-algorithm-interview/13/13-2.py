import math
import sys
from typing import List


# 주연경
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:

        values = []

        node = head
        while node:
            values.append(node.val)
            node = node.next

        return values[:] == values[::-1]
