class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        first = head

        while first:
            tmp = first.next
            first.next = prev
            prev = first
            first = tmp

        return prev