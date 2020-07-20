"""
Remove Linked List Elements
https://leetcode.com/explore/challenge/card/july-leetcoding-challenge/546/week-3-july-15th-july-21st/3396/
Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        # Solution 1 - 100 ms
        """
        if not head:
            return
        previous, current = None, head
        while current:
            if current.val == val:
                if previous:
                    previous.next = current.next
                    current = current.next
                else:
                    head = current.next
                    current = head
            else:
                previous = current
                current = current.next
        return head
        """
        # Solution 2 - 48 ms
        """
        dummy = ListNode(0)
        dummy.next = head

        prev, curr = dummy, head
        while curr:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        return dummy.next
        """
        # Solution 3 - 52 ms
        dumb = ListNode(None)
        dumb.next = head
        prev = dumb
        cur = head
        while cur:
            if cur.val == val:
                prev.next = cur.next
                cur = prev.next
            else:
                prev = prev.next
                cur = cur.next
        return dumb.next


# Main Call
# Load the linked list
head = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(6)
node4 = ListNode(3)
node5 = ListNode(4)
node6 = ListNode(5)
node7 = ListNode(6)

head.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7

val = 6

solution = Solution()
node = solution.removeElements(head, val)
temp = node
while temp:
    print(temp.val)
    temp = temp.next
