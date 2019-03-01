#! usr/local/bin/env python3
"""
    Object queue
    Kmom04
"""
from node import Node

class Queue():
    """class object to handle linked list as a queue"""

    def __init__(self):
        """initate the object"""
        self.head = None

    def enqueue(self, value):
        """1. add a value to the "beginning" of the queue"""
        #current är temporär variabel.

        # current = self.head
        new_node = Node(value)
        new_node.set_next(self.head)
        self.head = new_node

        # #kolla om current är första i listan. om inte lägg till nytt.
        # if current:
        #     while current.get_next() != None:
        #         current = current.get_next()
        #     print("inte första värdet, lägger till detta")
        #     current.set_next(new_node)
        # else:
        #     print("första värdet! lägger till! ")
        #     self.head = new_node

    def dequeue(self):
        """2. remove next in line with FIFO. First in First out."""

        prev = None
        current = self.head
        while current.get_next() != None:
            prev = current
            current = current.get_next()

        prev.set_next(current.get_next())

        current = None

        # Lite notes och eget innan try catch i Handle() i main.
        # if current:
        #     while current.get_next() != None:
        #         prev = current
        #         current = current.get_next() #stega framåt.
        # curr är ett steg före prev.
        #
        #     #nu är current på sista noden och prev är på noden innan.
        #     #länka om prev. till currents next.
        #     prev.set_next(current.get_next())
        #
        #     #sätt current node None så är den borta...
        #     current = None
        # else:
        #     print("finns inget att ta bort")

    def peek(self):
        """3. return next value"""
        current = self.head

        while current.get_next() != None:
            current = current.get_next()
        return current.get_data()

        # Lite notes och eget innan try catch i Handle() i main.
        # if current:
        #     while current.get_next()!= None:
        #         current = current.get_next()
        #     return current.get_data()
        # else:
        #     print("ska bli en exception som fångas i handler()")
        #     return False

    def size(self):
        """4. return size of linked list"""
        current = self.head

        if current:
            size = 1
            #så länge det inte är 1st or sist
            while current.get_next() != None:
                size += 1
                #stega framåt. när sista next är
                #sist blir det None och while loopen avslutas.
                current = current.get_next()

        else:
            size = 0
            print("det var första och borde därmed vara 0")

        return size

    def is_empty(self):
        """5. return true if list is empty. False otherwise"""
        current = self.head

        if current:
            return False

    def show_list(self):
        """print linked list."""

        current = self.head

        while current:
            print('Datan: {}'.format(current.get_data()))
            current = current.get_next()
