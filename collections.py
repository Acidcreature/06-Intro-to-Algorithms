"""
        **************************** Collection Types *************************************

Collection - a group of 0 or more items that can be treated as a conceptual unit. Strings, lists, tuples,
             dictionaries.

            other types: stacks, queues, priority queues, binary search trees, heaps, graphs, and bags.

Linear Collection: like people in a line, they are ordered by position. each item except the first has a
                   unique predecessor   ( D1 <- D2 <- D3 <- D4 <- D5 )

Hierarchical collection: ordered structure resembling an upside down tree each data item except 
                        the one at the top has just one predecessor called its parennt, but potentially has 
                        many successors called children.

Graph collection: aka. graph, each item can have many predecessors and many successors. These are also called
                  neighbors.

unordered collections: these are not in any particular order, and its not possible to meaningfully speak
                        of an items predecessor or successor.



        **************************** Operation Types *************************************

Determine the size: Use pythons len function to obtain the number of items currently in the collection

Test for item membership: Use pythons In operator to seach for given target in collection, returns True if found

Traverse a collection: Use pythons for loop to visit each item in the collection. The order for which items are visited
                        depends upon the type of collection.

Obtain a string representation: Use pythons str function to obrain a string representation.

test for equality: use pythons == to determine whether two collections are equal. Two collections are equal 
                    if they are of the same type and contain the same items. The order in which pairs of items
                    are compared depends on the type of collection.

concatenate two collections: use pythons + operator to obtain a new collection of the same type as the operands,
                            and containing the items in the two operands.

convert to another type of collection: Create a new collection with the same items as a source collection.

Insert an item: add the item to the collection, possibly at a given position.

remove an item: remove the item from the collection, possibly at a given position.

replace an item: combine removal and insertion into one operation.

Access or retrieve and item: Obtain an item, possibly at a given position.

"""