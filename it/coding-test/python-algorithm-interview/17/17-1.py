#김동억
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        init = latest = None
        if head and head.next:
            init = head.next
        else:
            return head
        while head and head.next:
            print(latest.val if latest else 'start', head.val, head.next.val)
            right_node = head.next
            head.next = right_node.next
            right_node.next = head
            if latest:
                latest.next = right_node

            latest = head
            head = head.next

        if head:
            latest.next = head
        return init
