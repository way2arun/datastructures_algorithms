"""
Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example 1:

Input: 1->2->3->4->5->NULL
Output: 1->3->5->2->4->NULL
Example 2:

Input: 2->1->3->5->6->4->7->NULL
Output: 2->3->6->7->1->5->4->NULL
Note:

The relative order inside both the even and odd groups should remain as it was in the input.
The first node is considered odd, the second node even and so on ...
https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/536/week-3-may-15th-may-21st/3331/
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        # Solution 1 - 48 ms
        """
        if head and head.next:
            even_head = head.next
            even_tail = even_head
        else:
            return head
        odd_tail = head

        while even_tail and even_tail.next:
            odd_tail.next = even_tail.next
            even_tail.next = even_tail.next.next
            even_tail = even_tail.next
            odd_tail = odd_tail.next
        odd_tail.next = even_head
        return head
        """
        # Solution 2
        """
        cur = head
        values = []
        while cur:
            values.append(cur.val)
            cur = cur.next

        i = 0
        cur = head
        while i < len(values):
            cur.val = values[i]
            cur = cur.next
            i += 2
        i = 1
        while i < len(values):
            cur.val = values[i]
            cur = cur.next
            i += 2
        return head
        """
        # Solution 3 25 ms
        odds = ListNode(0)
        evens = ListNode(0)

        oddHead = odds
        evenHead = evens

        length = 1

        while head:
            if length % 2 == 0:
                evens.next = head
                evens = evens.next
            else:
                odds.next = head
                odds = odds.next

            length += 1
            head = head.next

        # need to cut the end of the lists
        odds.next = None
        evens.next = None

        if odds:
            odds.next = evenHead.next
            return oddHead.next
        else:
            return evenHead.next

    def printList(self, head):
        temp = head
        while temp:
            print(temp.val)
            temp = temp.next


# Main Call
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

solution = Solution()

list_node = solution.oddEvenList(node1)
solution.printList(list_node)
