#! usr/local/bin/env python3
"""
    Assignment to create an unorderlist
    Kmom04
"""
from unorderedlist import UnorderedList
from error import OutOfIndex
from error import AttError
from error import WrongType
from error import NoValue


# linked_list = Queue()

class Handler():
    """handle the linked list"""

    def __init__(self):
        """initate object"""
        self.uol = UnorderedList()
        self.uol.add('ett')
        self.uol.add('två')

    def handle_is_empty(self):
        """1 is_empty: Returnera True/False för om listan är tom eller inte."""
        print('Is list empty? {}'. format(self.uol.is_empty()))
        return True

    def handle_add(self):
        """ 2 add: Lägg till nytt element/nod sist i listan."""
        value = (input('Add: '))
        self.uol.add(value)
        return True

    def handle_insert(self):
        """3 insert: Lägg till nytt element/nod på specifikt index.
        Om index inte finns lyft exception."""
        value = (input("New value: "))

        try:
            i = int(input("At index: "))
            self.uol.insert(value, i)
        except (ValueError, WrongType):
            print("Not an integer, try again!")
        except AttError:
            print("No value at that index.")

        return True

    def handle_set(self):
        """4 set: Skriv över element med ny data som finns på index.
        Om index inte finns lyft exception."""
        value = (input("New value: "))

        try:
            i = int(input("At index: "))
            self.uol.set(value, i)

        except (ValueError, WrongType):
            print("Not an integer, try again!")
        except AttError:
            print("No element at that index.")

    def handle_size(self):
        """5 size: Returnera antaler element i listan."""
        print('Number of elements in list: {}'.\
        format(self.uol.size()))

    def handle_get(self):
        """6 get: Returnera värde på index.
        Om index inte finns lyft exception."""

        try:
            i = int(input('Get element at index: '))

            element = self.uol.get(i)
            if element:
                print('Data at index: {}, is: {}'.\
                format(i, element))
        except (TypeError, ValueError):
            print("Not an integer, try again!")
        except OutOfIndex:
            print("Out of index.")

    def handle_index_of(self):
        """7 index_of: Om data finns i listan returnera dess index.
        Om nod med data inte finns lyft exception."""
        value = str(input("Get index of: "))
        value.strip()

        try:
            index = self.uol.index_of(value)

            if index:
                print('Your word is at index: {}'.\
                format(index))
        except NoValue:
            print('Could not find your word {}'.\
            format(value))

    def handle_print_list(self):
        """8 print_list: Skriv ut listans innehåll."""
        print(self.uol.print_list())

    def handle_remove(self):
        """9 remove: Ta bort nod med samma data.
        Om nod med data inte finns lyft exception."""

        value = input("Remove: ")
        value.strip() #remove whitespace

        try:
            self.uol.remove(value)
            print('Removed {}'.format(value))
        except NoValue:
            print('Could not remove {}'.\
            format(value))

    def handle_print_el(self):
        """print elements"""
        self.uol.print_el()


    def handle_input(self, choice):
        """handle user input"""

        if  choice == "1":
            self.handle_is_empty()

        elif choice == "2":
            self.handle_add()

        elif choice == "3":
            self.handle_insert()

        elif choice == "4":
            self.handle_set()

        elif choice == "5":
            self.handle_size()

        elif choice == "6":
            self.handle_get()

        elif choice == "7":
            self.handle_index_of()

        elif choice == "8":
            self.handle_print_list()

        elif choice == "9":
            self.handle_remove()

        elif choice == "p":
            self.handle_print_el()
        else:
            print("invalid choice.")



    def start(self):
        """eternal loop for menu until user shoose q or keyinterrupt"""

        while True:
            print("--------------------------\n"
                  + "1) check if list is empty. Return True/False.\n"
                  + "2) add a new value to the end of the list.\n"
                  + "3) insert new value at a specific index.\n"
                  + "4) replace a value at a specific index.\n"
                  + "5) get number of values in list.\n"
                  + "6) get value at a specific index.\n"
                  + "7) get index of specific value.\n"
                  + "8) print the entire list.\n"
                  + "9) remove node with your value.\n"
                  + "q) quit.\n")

            choice = (input("-->  "))
            if choice == "q":
                break
            elif choice is None:
                print("please enter your choice")
                continue
            else:
                self.handle_input(choice)

            # try:
            #     if choice == "q":
            #         break
            #     elif choice == "1":
            #         print('Is list empty? {}'. format(self.uol.is_empty()))
            #
            #     elif choice == "2":
            #         value = (input('Add: '))
            #         self.uol.add(value)
            #
            #     elif choice == "3":
            #         value = (input("New value: "))
            #
            #         try:
            #             i = int(input("At index: "))
            #             self.uol.insert(value, i)
            #         except (ValueError, WrongType):
            #             print("Not an integer, try again!")
            #         except AttError:
            #             print("No value at that index.")
            #
            #     elif choice == "4":
            #         value = (input("New value: "))
            #
            #         try:
            #             i = int(input("At index: "))
            #             self.uol.set(value, i)
            #
            #         except (ValueError, WrongType):
            #             print("Not an integer, try again!")
            #         except AttError:
            #             print("No element at that index.")
            #
            #     elif choice == "5":
            #         print('Number of elements in list: {}'.\
            #         format(self.uol.size()))
            #
            #     elif choice == "6":
            #         try:
            #             i = int(input('Get element at index: '))
            #
            #             element = self.uol.get(i)
            #             if element:
            #                 print('Data at index: {}, is: {}'.\
            #                 format(i, element))
            #         except (TypeError, ValueError):
            #             print("Not an integer, try again!")
            #         except OutOfIndex:
            #             print("Out of index.")
            #
            #     elif choice == "7":
            #         value = str(input("Get index of: "))
            #         value.strip()
            #
            #         try:
            #             index = self.uol.index_of(value)
            #
            #             if index:
            #                 print('Your word is at index: {}'.\
            #                 format(index))
            #         except NoValue:
            #             print('Could not find your word {}'.\
            #             format(value))
            #
            #     elif choice == "8":
            #         print(self.uol.print_list())
            #
            #     elif choice == "9":
            #         value = input("Remove: ")
            #         value.strip() #remove whitespace
            #
            #         try:
            #             self.uol.remove(value)
            #             print('Removed {}'.format(value))
            #         except NoValue:
            #             print('Could not remove {}'.\
            #             format(value))
            #
            #     elif choice == "p":
            #         self.uol.print_el()
            #     else:
            #         print("invalid choice.")
            #         continue
            #
            # except OutOfIndex:
            #     print("out of index")
            # except AttError:
            #     print("nothing in the list.")

game = Handler()
game.start()
