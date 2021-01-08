#주연경
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:

        node = head

        while node and node.next:
            node.val, node.next.val = node.next.val, node.val
            node = node.next.next

        return head
