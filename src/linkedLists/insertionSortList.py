"""
Insertion Sort List
Sort a linked list using insertion sort.


A graphical example of insertion sort. The partial sorted list (black) initially contains only the first element in the list.
With each iteration one element (red) is removed from the input data and inserted in-place into the sorted list


Algorithm of Insertion Sort:

Insertion sort iterates, consuming one input element each repetition, and growing a sorted output list.
At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list, and inserts it there.
It repeats until no input elements remain.

Example 1:

Input: 4->2->1->3
Output: 1->2->3->4
Example 2:

Input: -1->5->3->4->0
Output: -1->0->3->4->5

"""


# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        # Solution 1 - 1832 ms
        """
        dummy_head = ListNode()
        curr = head
        while curr:
            prev_pointer = dummy_head
            next_pointer = dummy_head.next
            while next_pointer:
                if curr.val < next_pointer.val:
                    break
                prev_pointer = prev_pointer.next
                next_pointer = next_pointer.next
            temp = curr.next
            curr.next = next_pointer
            prev_pointer.next = curr
            curr = temp
        return dummy_head.next
        """
        # Solution 2 - 40 ms
        mylist = []
        ptr = head
        while ptr:
            mylist.append(ptr.val)
            ptr = ptr.next

        mylist.sort()

        ptr = head
        for val in mylist:
            ptr.val = val
            ptr = ptr.next

        return head

    def printList(self, head):
        temp = head
        while (temp):
            print(temp.val)
            temp = temp.next



# Main Call
head = ListNode(4)
head.next =ListNode(2)
head.next.next = ListNode(1)
head.next.next.next = ListNode(3)

solution = Solution()
node = solution.insertionSortList(head)
print(solution.printList(node))
