
# Doubly Linked Lists - Very similar to Singly Linked, however these have prev pointer
#                        and a tail node.
#                        Move left, to previous node, from a given a node
#                        Move immediately to the last node

class DoubleNode:
    def __init__(self, data, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # Two cases to consider
    def append(self, data):
        newNode = DoubleNode(data)
        # Empty linked list?
        if self.head is None:
            newNode.prev = None
            self.head = newNode
            self.tail = self.head

        # We have items in our list
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = self.tail.next

    def prepend(self, data):
        newNode = DoubleNode(data)
        # Empty linked list?
        if self.head is None:
            newNode.prev = None
            self.head = newNode
            self.tail = self.head
        # anything in our linked list
        newNode.next = self.head
        self.head.prev = newNode
        self.head = newNode
        

    # Inserting within linked list
    def insert_node(self, index, data):
        # Is linked list empty or index less than 0
        if self.head is None or index <= 0:
            self.head = DoubleNode(data, self.head)
        # find our position to insert
        else:
            probe = self.head
            while index > 1 and probe.next != None:
                probe = probe.next
                index -= 1
            probe.next = DoubleNode(data, probe.next, probe)
            if probe.next.next == None:
                self.tail = probe.next
            else:
                probe.next.next.prev = probe.next

    def delete_node(self, index):
        # Is this the only node
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



    def print_linked_list(self):
        probe = self.head
        while probe != None:
            print(probe.data)
            probe = probe.next



doubly_linked_list = DoublyLinkedList()
doubly_linked_list.append("1")
doubly_linked_list.append("2")
doubly_linked_list.prepend("3")
doubly_linked_list.append("4")
doubly_linked_list.insert_node(3, "5")
doubly_linked_list.prepend("6")
doubly_linked_list.insert_node(7, "7")
doubly_linked_list.append("8")
doubly_linked_list.delete_node(0)
doubly_linked_list.delete_node(1)
doubly_linked_list.delete_node(7)
doubly_linked_list.print_linked_list()


