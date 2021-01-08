#주연경
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:

        if head == None:
            return head

        odd = head
        even = head.next
        even_head = even

        while even and even.next:
            odd.next = odd.next.next
            even.next = even.next.next

            odd = odd.next
            even = even.next

        odd.next = even_head
        return head
