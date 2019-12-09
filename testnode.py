# This file will test the Node Class

from node import Node

head = None

# Add five nodes to the beginning of the linked structure
for count in range(1, 6):
    head = Node(count, head)

# pring the contents of the structure
while head != None:
    print(head.data)
    head = head.next

"""
- One pointer, head, generates the linked structure. This pointer is manipulated
    in such a way that the most recently inserted item is always at the begining of the
    structure
- When the data is displayed, they appear in the reverse order of their insertion
- Also, when the data is displayed, the head pointer is reset to the next node, until
    effectively deleted from the linked structure. They are no longer available to 
    to the program and are recycled during the next garbage collection.
"""