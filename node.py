
# this class will represent a singly linked node

class Node:
    def __init__(self, data, next = None):
        # Instantiates a Node with a default next of None
        self.data = data
        self.next = next

# The LinkedList class will instantiate Node objects and we'll add methods
# to this class to add functionality

class LinkedList:
    def __init__(self):
        self.head = None

    # Add things to the end of our linked list
    def append(self, data):
        # Instantiate a new Node
        newNode = Node(data)
        # Is there something in our linkedlist yet?
        if self.head is None:
            self.head = newNode
        # There are node(s) in our linked list
        else:
            # Initialize our probe pointer
            probe = self.head
            # Is probe at the end of the linked list
            while probe.next != None:
                probe = probe.next
            probe.next = newNode


    # printing our linked list
    def print_linked_list(self):
        probe = self.head
        while probe != None:
            print(probe.data)
            probe = probe.next

    # Add things to the beginning 
    def prepend(self, data):
        # instnatiate a new Node object
        newNode = Node(data)
        # anything in our linked list
        newNode.next = self.head
        self.head = newNode

    # Inserting within linked list
    def insert_node(self, index, data):
        # Is linked list empty or index less than 0
        if self.head is None or index <= 0:
            self.head = Node(data, self.head)
        # find our position to insert
        else:
            probe = self.head
            while index > 1 and probe.next != None:
                probe = probe.next
                index -= 1
            probe.next = Node(data, probe.next)

    # Remove a node
    def delete_node(self, index):
        # Is this the only node?
        if index <= 0 or self.head.next is None:
            removedItem = self.head.data
            self.head = self.head.next
            return removedItem
        else:
            probe = self.head
            while index > 1 and probe.next.next != None:
                probe = probe.next
                index -= 1
            removedItem = probe.next.data
            probe.next = probe.next.next
            return removedItem




#linked_list = LinkedList()
#linked_list.append("A")
#linked_list.append("Hello")
#linked_list.prepend("I should be at the beginning")
#linked_list.prepend("Now I'm first")
#linked_list.insert_node(2, "Inserted")
#linked_list.insert_node(24, "next insert")
#linked_list.delete_node(1)
#
#
#linked_list.print_linked_list()


# Just an empty link
node1 = None

# A node containing data and an empty link
node2 = Node("A", None)
node3 = Node("B", node2)

#print(node3.data)

"""
Circular Linked List - Special case of singly linked list.
                        Insertion and removal of the first node are 
                        special cases of the insert ith and remove ith
                        operations on a singly linked list. These are special
                        because the head pointer must be reset. You can use circular linked lists
                        with a dummy header node. Contains a link from the last node
                        back to the first node in the structure.
"""

class CircularLinked:
    def __init__(self):
        self.head = None
       
    
    def append(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            self.head.next = self.head
        else:
            probe = self.head
            while probe.next != self.head:
                probe = probe.next
            probe.next = newNode
            newNode.next = self.head

    def print_linked_list(self):
        probe = self.head
        while probe.next != self.head:
            print(probe.data)
            probe = probe.next
        print(probe.data)

circly_linked_list = CircularLinked()
circly_linked_list.append(1)
circly_linked_list.append(2)
circly_linked_list.print_linked_list()
