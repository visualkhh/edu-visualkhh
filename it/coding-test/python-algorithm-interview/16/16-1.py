#주연경

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        u = 0
        root = head = ListNode(0)

        while l1 or l2 or u:

            l1, val1 = [l1.next, l1.val] if l1 else [0, 0]
            l2, val2 = [l2.next, l2.val] if l2 else [0, 0]

            u,d = divmod(val1 + val2 + u, 10)

            head.next = ListNode(d)
            head = head.next

        return root.next

