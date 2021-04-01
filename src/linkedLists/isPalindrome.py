"""
Palindrome Linked List
Given the head of a singly linked list, return true if it is a palindrome.



Example 1:


Input: head = [1,2,2,1]
Output: true
Example 2:


Input: head = [1,2]
Output: false


Constraints:

The number of nodes in the list is in the range [1, 105].
0 <= Node.val <= 9


Follow up: Could you do it in O(n) time and O(1) space?

"""


# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def reverse(self, head):
        prev = None
        while head:
            nextNode = head.next
            head.next = prev
            prev = head
            head = nextNode
        return prev
    def isPalindrome(self, head: ListNode) -> bool:
        # Solution 1 - 796 ms
        """
        slow = fast = head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        if fast != None:  # case number of elements is odd, move mid to next element.
            slow = slow.next

        def reverse(head):
            ans = None
            while head != None:
                next = head.next
                head.next = ans
                ans = head
                head = next
            return ans

        head2 = reverse(slow)  # slow is our mid
        while head2 != None:
            if head.val != head2.val:
                return False
            head = head.next
            head2 = head2.next
        return True
        """
        # Solution 2 - 40 ms
        if not head:
            return True
        firstHalf = slow = fast = head

        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        secondHalf = self.reverse(slow.next)

        while secondHalf and firstHalf:
            if secondHalf.val != firstHalf.val:
                return False
            secondHalf = secondHalf.next
            firstHalf = firstHalf.next
        return True


# Main Call
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(2)
head.next.next.next = ListNode(1)

solution = Solution()
print(solution.isPalindrome(head))