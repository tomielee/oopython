#! usr/local/bin/env python3
"""
    Object unordered list
    Copied from Kmom04, assignment 2
    to kmmom05, assignment 2
"""
from node import Node
from error import OutOfIndex
from error import AttError
from error import NoValue

class UnorderedList():
    """listobject to handle unorders lists"""

    def __init__(self):
        """initate the object"""
        self.head = None


    def is_empty(self):
        """1. return true if list is empty. False otherwise"""
        # is_empty: Returnera True/False för om listan är tom eller inte.

        current = self.head

        if current:
            return False

        return True

    def add(self, value):
        """2. add a value to the end of the list. all values are string!"""
        # add: Lägg till nytt element/nod sist i listan.

        current = self.head
        new_node = Node(str(value))
        #kolla om current är första i listan. om inte lägg till nytt.
        if current:
            while current.get_next() != None:
                current = current.get_next()
            current.set_next(new_node)
        else:
            self.head = new_node

    def insert(self, value, i):
        """3. insert new value at a specifik index"""
        # insert: Lägg till nytt element/nod på specifikt index.
        # Om index inte finns lyft exception.

        current = self.head
        new_node = Node(value)
        temp = None
        counter = 0

        while counter < i:
            if i > self.size():
                raise AttError
            temp = current #steget bakom current
            current = current.get_next() #då current stegar framåt
            counter += 1

        if i == 0:
            self.head = new_node
            new_node.set_next(current)
        elif counter == i:
            temp.set_next(new_node) #temp pekar på ny node
            new_node.set_next(current) #ny node pekar på current
        else:
            raise AttError


    def set(self, value, i):
        """4. replace a node data with new value at at specific index"""
        # set: Skriv över element med ny data som finns på index.
        # Om index inte finns lyft exception.
        current = self.head
        new_node = Node(value)
        temp = None

        counter = 0

        while counter < i:
            if i > self.size():
                raise AttError
            temp = current
            current = current.get_next()
            counter += 1

        if i == 0:
            self.head = new_node
            new_node.set_next(current.get_next())
            current = None
        elif counter == i:
            temp.set_next(new_node)
            current = current.get_next()
            new_node.set_next(current)
        else:
            raise AttError


    def size(self):
        """5. return size of linked list"""
        # size: Returnera antaler element i listan.

        current = self.head

        if current:
            size = 1
            while current.get_next() != None:
                size += 1
                current = current.get_next()
        else:
            size = 0

        return size

    def get(self, i):
        """6. return data at index from user"""
        # get: Returnera värde på index. Om index inte finns lyft exception.

        current = self.head

        counter = 0

        while counter < i:
            if i > self.size():
                raise OutOfIndex
            current = current.get_next()
            counter += 1

        if i == 0:
            value = current.get_data()
            return value
        elif counter == i:
            value = current.get_data()
            return value


    def index_of(self, value):
        """7. return index of a value from user"""
        # index_of: Om data finns i listan returnera dess index.
        # Om nod med data inte finns lyft exception.
        current = self.head
        index = 0

        while current != None:
            if current.get_data() == value:
                return index

            index += 1
            current = current.get_next()

        raise NoValue


    def print_list(self):
        """8.print linked list."""
        # print_list: Skriv ut listans innehåll.

        current = self.head
        li = []

        while current:
            li.append(current.get_data())
            current = current.get_next()

        return li


    def remove(self, value):
        """9. remove node with user input value"""
        # remove: Ta bort nod med samma data.
        # Om nod med data inte finns lyft exception.

        current = self.head
        prev = None

        while current:
            if current.get_data() == value:
                if prev:
                    prev.set_next(current.get_next())
                    current = None
                else:
                    self.head = current.get_next()
                return True
            prev = current
            current = current.get_next()

        raise NoValue


    def print_el(self):
        """print elements in list"""
        current = self.head

        while current:
            print(current.get_data())
            current = current.get_next()


    # def __len__(linked_list):
    #     """return int value, length of list"""
    #     current = linked_list.head
    #
    #     if current:
    #         len = 1
    #         while current.get_next() != None:
    #             len += 1
    #             current = current.get_next()
    #     else:
    #         len = 0
    #
    #     return len
    #
    # def __getitem__(linked_list, key):
    #     """return index of key"""
    #     current = linked_list.head
    #
    #     counter = 0
    #
    #     while counter < key:
    #         if key > len(linked_list):
    #             raise OutOfIndex
    #         current = current.get_next()
    #         counter += 1
    #
    #     if key == 0:
    #         return int(current.get_data())
    #     elif counter == key:
    #         return current.get_data()
    #
    # def __setitem__(self, value, key):
    #     """replace a  data with new value at at specific index"""
