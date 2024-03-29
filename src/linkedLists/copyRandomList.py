"""
Copy List with Random Pointer
A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.
Your code will only be given the head of the original linked list.



Example 1:


Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
Example 2:


Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]
Example 3:



Input: head = [[3,null],[3,0],[3,null]]
Output: [[3,null],[3,0],[3,null]]
Example 4:

Input: head = []
Output: []
Explanation: The given linked list is empty (null pointer), so return null.


Constraints:

0 <= n <= 1000
-10000 <= Node.val <= 10000
Node.random is null or is pointing to some node in the linked list.
   Hide Hint #1
Just iterate the linked list and create copies of the nodes on the go. Since a node can be referenced from multiple nodes due to the random pointers, make sure you are not making multiple copies of the same node.
   Hide Hint #2
You may want to use extra space to keep old node ---> new node mapping to prevent creating multiples copies of same node.
   Hide Hint #3
We can avoid using extra space for old node ---> new node mapping, by tweaking the original linked list. Simply interweave the nodes of the old and copied list. For e.g.
Old List: A --> B --> C --> D
InterWeaved List: A --> A' --> B --> B' --> C --> C' --> D --> D'
   Hide Hint #4
The interweaving is done using next pointers and we can make use of interweaved structure to get the correct reference nodes for random pointers.
"""


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def printList(self, head):
        print("Cloned List ")
        temp = head
        while temp:
            if temp.random == None:
                print(f'{temp.val} --> {temp.random}')
            else:
                random = temp.random
                print(f'{temp.val} --> {random.val}')
            temp = temp.next

    def copyRandomList(self, head: 'Node') -> 'Node':
        # Solution 1 - 40 ms
        """
        if not head:
            return None
        curr = head
        while curr:
            tmp = Node(curr.val)
            tmp.next = curr.next
            curr.next = tmp
            curr = tmp.next

        curr = head
        while curr:
            curr.next.random = curr.random.next if curr.random else None
            curr = curr.next.next

        node = head.next
        while node.next:
            node.next = node.next.next
            node = node.next

        return head.next
        """
        # Solution 2 - 16 ms
        if not head:
            return None

        hash_table = dict()
        m = n = head

        while m:
            hash_table[m] = Node(m.val)
            m = m.next

        while n:
            # if n.next in hash_table:
            #     hash_table[n].next = hash_table[n.next]
            # if n.random in hash_table:
            #     hash_table[n].random = hash_table[n.random]

            hash_table[n].next = hash_table.get(n.next)
            hash_table[n].random = hash_table.get(n.random)
            n = n.next

        return hash_table[head]


# Main Call
node = Node(7)
node.next = Node(13)
node.next.next = Node(11)
node.next.next.next = Node(10)
node.next.next.next.next = Node(1)

# 7's random points to Null
node.random = None
# 13's random points 7
node.next.random = node
# 11's random points 10
node.next.next.random = node.next.next.next
# 10's random point to 11
node.next.next.next.random = node.next.next
# 1's random point to 7
node.next.next.next.next.random = node

solution = Solution()
nodes = solution.copyRandomList(node)

solution.printList(nodes)
