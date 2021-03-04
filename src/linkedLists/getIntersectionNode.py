"""
 Intersection of Two Linked Lists
Write a program to find the node at which the intersection of two singly linked lists begins.

For example, the following two linked lists:


begin to intersect at node c1.



Example 1:


Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
Output: Reference of the node with value = 8
Input Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect). From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,6,1,8,4,5]. There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.


Example 2:


Input: intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
Output: Reference of the node with value = 2
Input Explanation: The intersected node's value is 2 (note that this must not be 0 if the two lists intersect). From the head of A, it reads as [1,9,1,2,4]. From the head of B, it reads as [3,2,4]. There are 3 nodes before the intersected node in A; There are 1 node before the intersected node in B.


Example 3:


Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
Output: null
Input Explanation: From the head of A, it reads as [2,6,4]. From the head of B, it reads as [1,5]. Since the two lists do not intersect, intersectVal must be 0, while skipA and skipB can be arbitrary values.
Explanation: The two lists do not intersect, so return null.


Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Each value on each linked list is in the range [1, 10^9].
Your code should preferably run in O(n) time and use only O(1) memory.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def printList(self, node):
        temp = node
        print(temp)
        while temp:
            print(temp.val)
            temp = temp.next

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # Solution 1 - 156 ms
        """
        if not headA or not headB: return None
        a = headA
        b = headB
        swaps = 0

        while swaps < 3:
            if a == b: return a
            a = a.next
            b = b.next
            if not a:
                swaps += 1
                a = headB
            if not b:
                swaps += 1
                b = headA

        return None
        """
        # Solution 2 - 132 ms
        """
        currA = headA
        currB = headB
        hashT = {}
        while currA:
            hashT[currA] = currB
            currA = currA.next
        while currB:
            if currB in hashT:
                return currB
            currB = currB.next
        """

        # Solution 3 - 132 ms
        currA = headA
        currB = headB
        while currA:
            while currB:
                if currA == currB:
                    return currA
                else:
                    currB = currB.next
            currB = headB
            currA = currA.next


# Main Call
headA = ListNode(4)
headA.next = ListNode(1)
headA.next.next = ListNode(8)
headA.next.next.next = ListNode(4)
headA.next.next.next.next = ListNode(5)

headB = ListNode(5)
headB.next = ListNode(6)
headB.next.next = ListNode(1)
headB.next.next.next = ListNode(8)
headB.next.next.next.next = ListNode(4)
headB.next.next.next.next.next = ListNode(5)

solution = Solution()
nodes = solution.getIntersectionNode(headA, headB)
solution.printList(headA)
solution.printList(headB)
print(nodes)
solution.printList(nodes)