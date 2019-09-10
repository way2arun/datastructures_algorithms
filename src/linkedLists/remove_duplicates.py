"""

Remove Dups: Write code to remove duplicates from an unsorted linked list.

"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None

    # Linked List append function
    def append(self, data: object) -> object:
        if self.last_node is None:
            self.head = Node(data)
            self.last_node = self.head
        else:
            self.last_node.next = Node(data)
            self.last_node = self.last_node.next

    # Function to get the previous node in the linked list
    def get_prev_node(self, ref_node: object) -> object:
        current = self.head
        while current and current.next != ref_node:
            current = current.next
        return current

    # Function to remove the node from the linked list
    def remove(self, node: object) -> object:
        prev_node = self.get_prev_node(node)
        if prev_node is None:
            self.head = self.head.next
        else:
            prev_node.next = node.next

    # Function to display the linked list
    def display(self):
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next


# Function to remove the duplicates from the linked list
# Time Complexity - O(n)
# Space Complexity - O(n)

def remove_duplicates(llist: object) -> object:
    first_node_pointer = llist.head
    while first_node_pointer:
        data = first_node_pointer.data
        next_node_pointer = first_node_pointer.next
        while next_node_pointer:
            if next_node_pointer.data == data:
                llist.remove(next_node_pointer)
            next_node_pointer = next_node_pointer.next
        first_node_pointer = first_node_pointer.next


# Driver Code
linked_list = LinkedList()
data_llist = input('Enter the Elements in the Linked List (Use Spaces) : ').split()
for data in data_llist:
    linked_list.append(int(data))

# Remove Duplicates
remove_duplicates(linked_list)

print('Updated Linked Lists - after duplicates removed: ')
linked_list.display()