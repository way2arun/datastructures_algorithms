"""
Sort List
Given the head of a linked list, return the list after sorting it in ascending order.

Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?



Example 1:


Input: head = [4,2,1,3]
Output: [1,2,3,4]
Example 2:


Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]
Example 3:

Input: head = []
Output: []


Constraints:

The number of nodes in the list is in the range [0, 5 * 104].
-105 <= Node.val <= 105
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def get_Middle(self, head):
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None
        return mid

    def get_Merge(self, head1, head2):
        dummy = tail = ListNode(None)
        while head1 and head2:
            if head1.val < head2.val:
                tail.next, tail, head1 = head1, head1, head1.next
            else:
                tail.next, tail, head2 = head2, head2, head2.next

        tail.next = head1 or head2
        return dummy.next

    def sortList(self, head: ListNode) -> ListNode:
        # Solution 1 - 220 ms
        """
        if not head or not head.next:
            return head
        mid = self.get_Middle(head)
        left = self.sortList(head)
        right = self.sortList(mid)
        return self.get_Merge(left, right)
        """
        # Solution 2 - 64 ms
        elems = []
        curr = head
        while curr:
            elems.append(curr.val)
            curr = curr.next
        elems.sort()
        curr = head
        for n in elems:
            curr.val = n
            curr = curr.next
        return head


# Main Call
head = ListNode(4)
node2 = ListNode(2)
node3 = ListNode(1)
node4 = ListNode(3)
head.next = node2
node2.next = node3
node3.next = node4

solution = Solution()
result = solution.sortList(head)
temp = result
while temp:
    print(temp.val)
    temp = temp.next
