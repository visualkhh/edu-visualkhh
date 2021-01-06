#김동억

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        rest = 0
        head = prev = cur = None
        while l1 or l2:
            cur = ListNode()
            if not head:
                head = cur
            else:
                prev.next = cur
            sum = (l1.val if l1 else 0) + (l2.val if l2 else 0) + rest
            if  sum >= 10:
                sum = sum - 10
                rest = 1
            else:
                rest = 0
            cur.val = sum
            l1,l2 = (l1.next if l1 else None), (l2.next if l2 else None)
            prev = cur

        if rest == 1:
            cur = ListNode(rest)
            prev.next = cur
        return head
