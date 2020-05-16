class Node:
    def __init__(self, val):
        self.val = val
        self.next = None  # the pointer initially points to nothing

# Linked List class contains a Node object
class LinkedList:
    # Function to initialize head
    def __init__(self):
        self.head = None
        # This function prints contents of linked list
        # starting from head

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.val)
            temp = temp.next





llist = LinkedList()

llist.head = Node(12)
second= Node(22)
third = Node(33)

llist.head.next = second
second.next = third

llist.printList()