#김동억
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        odd_cur = head
        even_cur = even_head = head.next
        while even_cur and even_cur.next:
            odd_cur.next, even_cur.next = odd_cur.next.next, even_cur.next.next
            odd_cur = odd_cur.next
            even_cur = even_cur.next
        odd_cur.next = even_head
        return head
