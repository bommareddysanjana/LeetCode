class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        lst = []
        while head:
            lst.append(head)
            head = head.next
        i = 0
        j = len(lst) - 1
        flag = True
        while(i<j):
            if (lst[i].val!=lst[j].val):
                flag = False
                break
            i += 1
            j -= 1
        return flag
