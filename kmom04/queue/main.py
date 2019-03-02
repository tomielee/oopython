#! usr/local/bin/env python3
"""
    Assignment to create a list, acting like a queue
    with linked list.
    Kmom04
"""
from queue import Queue
from errors import OutOfIndex
from errors import AttError


# linked_list = Queue()

class Handler():
    """handle the linked list as a queue"""

    def __init__(self):
        """initate object"""
        self.linked_list = Queue()

    def handle_add(self):
        """call on method add"""
        value = (input("Add: "))
        self.linked_list.enqueue(value)

    def handle_dequeue(self):
        """call on method remove"""

        if self.linked_list.dequeue():
            print("Removed first in queue.")
        else:
            raise AttError

    def handle_peek(self):
        """call on method peek"""
        if self.linked_list.peek():
            print('Peek: {}'.format(self.linked_list.peek()))
        else:
            raise AttError

    def handle_size(self):
        """return size"""
        print('Size of linked list: {}'.\
        format(self.linked_list.size()))

    def handle_is_empty(self):
        """call on function to return true if list is empty"""
        print('List is empty? {}'.\
        format(self.linked_list.is_empty()))

    def handle_show_list(self):
        """print list"""
        print(self.linked_list.show_list())


    def handle_input(self, choice):
        """handle input from user"""

        try:
            if choice == "1":
                self.handle_add()

            elif choice == "2":
                self.handle_dequeue()

            elif choice == "3":
                self.handle_peek()

            elif choice == "4":
                self.handle_size()

            elif choice == "5":
                self.handle_is_empty()

            elif choice == "6":
                self.handle_show_list()
            else:
                print("invalid choice.")
        except (AttError, OutOfIndex):
            print("No more values")

    def start(self):
        """menu"""

        while True:
            print("--------------------------")
            print("Meny.")
            print("1) Lägg till ett värde.")
            print("2) Ta bort nästa värde.")
            print("3) Kolla på FÖRSTA värde.")
            print("4) Storlek.")
            print("5) Empty?")
            print("q) Quit.")

            choice = (input("-->  "))

            if choice == "q":
                break
            elif choice is None:
                print("no input, try again")
                continue
            else:
                self.handle_input(choice)

            # try:
            #     if choice == "q":
            #         break
            #     elif choice == "1":
            #         value = (input("Add: "))
            #         self.linked_list.enqueue(value)
            #     elif choice == "2":
            #         self.linked_list.dequeue()
            #         print("Removed last object.")
            #         # else:
            #         #     raise AttError
            #     elif choice == "3":
            #         print('Peek: {}'.format(self.linked_list.peek()))
            #     elif choice == "4":
            #         print('Size of linked list: {}'.\
            #         format(self.linked_list.size()))
            #     elif choice == "5":
            #         print('List is empty? {}'.\
            #         format(self.linked_list.is_empty()))
            #     elif choice == "6":
            #         print(self.linked_list.show_list())
            #     else:
            #         print("invalid choice.")
            #         continue
            # except OutOfIndex:
            #     print("out of index")
            # except AttError:
            #     print("nothing in the list.")

game = Handler()
game.start()
