#! usr/local/bin/env python3
"""
    Assignment to create a list, acting like a queue
    with linked list.
    Kmom04
"""
from queue import Queue
from error import OutOfIndex
from error import AttError


# linked_list = Queue()

class Handler():
    """handle the linked list as a queue"""

    def __init__(self):
        """initate object"""
        self.linked_list = Queue()

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


            try:
                if choice == "q":
                    break
                elif choice == "1":
                    value = (input("Add: "))
                    self.linked_list.enqueue(value)
                elif choice == "2":
                    self.linked_list.dequeue()
                    print("Removed last object.")
                elif choice == "3":
                    print('Peek: {}'.format(self.linked_list.peek()))
                elif choice == "4":
                    print('Size of linked list: {}'.\
                    format(self.linked_list.size()))
                elif choice == "5":
                    print('List is empty? {}'.\
                    format(self.linked_list.is_empty()))
                elif choice == "6":
                    print(self.linked_list.show_list())
                else:
                    print("invalid choice.")
                    continue
            except OutOfIndex:
                print("out of index")
            except AttError:
                print("nothing in the list.")

game = Handler()
game.start()
