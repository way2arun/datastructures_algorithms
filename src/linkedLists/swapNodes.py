"""
 Swapping Nodes in a Linked List
You are given the head of a linked list, and an integer k.

Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from the end (the list is 1-indexed).



Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [1,4,3,2,5]
Example 2:

Input: head = [7,9,6,6,7,8,3,0,9,5], k = 5
Output: [7,9,6,6,8,7,3,0,9,5]
Example 3:

Input: head = [1], k = 1
Output: [1]
Example 4:

Input: head = [1,2], k = 1
Output: [2,1]
Example 5:

Input: head = [1,2,3], k = 2
Output: [1,2,3]


Constraints:

The number of nodes in the list is n.
1 <= k <= n <= 105
0 <= Node.val <= 100
   Hide Hint #1
We can transform the linked list to an array this should ease things up
   Hide Hint #2
After transforming the linked list to an array it becomes as easy as swapping two integers in an array then rebuilding the linked list

"""


# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def printList(self, head):
        temp = head
        while temp:
            print(temp.val)
            temp = temp.next

    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        # Solution 1 - 1068 ms
        """
        n = 0
        beg = head
        while beg:
            if n == k - 1: l = beg
            beg = beg.next
            n += 1

        r = head
        for m in range(n - k):
            r = r.next

        l.val, r.val = r.val, l.val
        return head
        """
        # Solution 2 - 964 ms
        slow, fast = head, head
        for _ in range(k - 1):
            fast = fast.next
        node1 = fast
        while fast.next:
            slow = slow.next
            fast = fast.next
        node2 = slow
        node1.val, node2.val = node2.val, node1.val
        return head


# Main Call
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

k = 2
solution = Solution()
node = solution.swapNodes(head, k)
solution.printList(node)
