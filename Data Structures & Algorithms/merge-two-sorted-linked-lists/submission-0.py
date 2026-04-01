class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        lis1_curr, lis2_curr = list1, list2

        dummy = ListNode(-1)
        res = dummy
        while lis1_curr or lis2_curr:
            if not lis1_curr and lis2_curr:
                res.next = lis2_curr
                break
            elif not lis2_curr and lis1_curr:
                res.next = lis1_curr
                break
            elif lis1_curr.val < lis2_curr.val:
                res.next = lis1_curr
                lis1_curr = lis1_curr.next
            else:
                res.next = lis2_curr
                lis2_curr = lis2_curr.next
            res = res.next

        return dummy.next