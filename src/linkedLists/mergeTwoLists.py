"""
Merge Two Sorted Lists
Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.



Example 1:


Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: l1 = [], l2 = []
Output: []
Example 3:

Input: l1 = [], l2 = [0]
Output: [0]


Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both l1 and l2 are sorted in non-decreasing order.
"""


# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


class Solution:
    def print_nodes(self, node):
        node_list = []
        while node:
            print(node.val)
            node_list.append(node.val)
            node = node.next
        print(node_list)
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Solution 1 - 36 ms
        """
        # create a new linkedlist which is used to store the result
        # here I have used two refereces to the same list since I should return the root of the list
        # head will be used during the process and res will be returned
        head = res = ListNode(0)

        # this is the loop which will compare the two list and add the value to the result
        # here we will check is l1.val <= l2.val if yes then we will add l1 to the head
        # else we will add l2 to the list
        while l1 and l2:
            if l1.val <= l2.val:
                head.next = l1
                head = head.next
                l1 = l1.next
            else:
                head.next = l2
                head = head.next
                l2 = l2.next

        # if there is only l1 then we need not check with l2 we can directly append all the values of l1
        if l1:
            head.next = l1
            head = head.next

        # if there is no l1 then we can add all the l2 to the result
        else:
            head.next = l2
            head = head.next

        # we have to return the res.next since initally we created a dummy node called 0  res = ListNode(0)
        return res.next
        """
        # Solution 2 - 16 ms
        # Catch cases where one list is None
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        # Save the head node to return
        head = l2 if l2.val <= l1.val else l1

        while l1 is not None and l2 is not None:

            # Compare l1 and l2
            bigger = l1 if l1.val >= l2.val else l2
            smaller = l1 if bigger is l2 else l2

            # Find the right spot for the bigger node in the smaller list
            while smaller.next is not None and smaller.next.val <= bigger.val:
                smaller = smaller.next

            # Save the rest of the smaller list
            l1 = smaller.next

            # Splice in the bigger node here
            smaller.next = bigger
            l2 = smaller.next

        return head


# Main Call
l1 = ListNode(val=1)
l1.next = ListNode(val=2)
l1.next.next = ListNode(val=4)

l2 = ListNode(val=1)
l2.next = ListNode(val=3)
l2.next.next = ListNode(val=4)

solution = Solution()
new_node_list = solution.mergeTwoLists(l1, l2)
solution.print_nodes(new_node_list)
