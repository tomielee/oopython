#! usr/local/bin/env python3
"""
    Spellchecker classobject as main function for
    wordprogram.
    Kmom10 2019
"""
from trie import Trie

class SpellChecker():
    """main object for spellchecker"""

    def __init__(self):
        """constructor for SpellChecker()"""
        self.d = Trie()
        self.start()

    def start(self):
        """
            default start with textfile
            words.txt
        """

        self.set_new_dict("words.txt")
        self.show_menu()


    def handle_search_word(self):
        """
            MENU 1. SEARCH WORD
            word: user input
            return: bool. True if word exists in dictionary.
        """
        word = input("search for: ")

        if self.d.search_word(word.lower().strip()):
            print('your word "{}"" is in the dictionary.'.format(word))
        else:
            print('could not find your word "{}"'.format(word))

    def handle_start_with(self):
        """
            MENU 2. SEARCH WORDS WITH PREFIX
            prefix: user input
            return: a list of 10 words
        """
        prefix = ""

        while prefix[-4:] != "quit":

            prefix = prefix + input("search for: " + prefix)

            words = self.d.start_with(prefix.lower().strip())
            if words:
                print('\nsearch result, 10 words starting with "{}" '.format(prefix.upper()))
                for word in words:
                    print(word)
            else:
                print('there are now words starting with  "{}"'.format(prefix.upper()))
                break

    def handle_set_new_dict(self):
        """
             MENU 3. CHANGE DICTIONARY
             choice = user input - filename
        """
        print("Enter the filename:")
        print("Available are: dictionary.txt and tiny_dictionary.txt")
        self.set_new_dict(input("enter the name: "))

    def set_new_dict(self, choice):
        """
            MENU 3. CHANGE DICTIONARY
            choice = user input - filename
        """
        self.d = None
        self.d = Trie()

        content = self._read_file(choice) #hämtar innehållet
        words = content.split("\n") #skapar en lista med ord
        for word in words:
            # print('new word: {}'.format(word))
            self.d.add(word)

    @staticmethod
    def _read_file(choice):
        """
            private method read file
        """
        content = SpellChecker._open_file(choice) #ingen whitespace
        fh = open(choice)
        content = fh.read().strip() #läser innehåll utan whitespace
        fh.close()
        return content

    @staticmethod
    def _open_file(choice):
        """
            open file. nothing else.
        """
        try:
            fh = open(choice)
            fh.close()
        except FileNotFoundError:
            print('filen finns inte')

        return value

    def handle_print(self):
        """
            MENU 4. PRINT ALL WORDS
            Print: list of all words.
        """
        words_to_print = self.d.print_nodes()

        print("PRINT: \n")
        for word in words_to_print:
            print(word)

    def handle_input(self, choice):
        """
            handle user choice from menu
        """

        if choice == "1":
            self.handle_search_word()

        elif choice == "2":
            self.handle_start_with()

        elif choice == "3":
            self.handle_set_new_dict()

        elif choice == "4":
            self.handle_print()

        else:
            print("invalid choice")


    def show_menu(self):
        """eternity loop to show menu"""
        while True:
            print("--------------------------\n"
                  + "1) check if word is dictionary\n"
                  + "2) get a suggestion of word. \n"
                  + "3) change dictionary. \n"
                  + "4) print all words in dictionary. \n"
                  + "q) quit.\n")

            choice = (input("-->  "))
            if choice == "q":
                break
            elif choice is None:
                print("please enter your choice")
                continue
            else:
                self.handle_input(choice)

nytt = SpellChecker()
# nytt.set_new_dict("words.txt")
# nytt.show_menu()
