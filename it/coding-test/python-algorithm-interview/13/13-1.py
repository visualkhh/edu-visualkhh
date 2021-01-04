import math
import sys
from typing import List


# 김동억
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        stack = []
        while head:
            stack.append(head.val)
            head = head.next
        if not stack or stack == stack[::-1]:
            return True
        else: return False
