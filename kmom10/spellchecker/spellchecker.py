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

    def set_new_dict(self, choice):
        """
            MENU 4. CHANGE WORDS
            use a new file
        """
        self.d = None
        self.d = Trie()

        content = self._read_file(choice) #hämtar innehållet
        words = content.split("\n") #skapar en lista med ord
        for word in words:
            print('new word: {}'.format(word))
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
        value = 'No'
        try:
            fh = open(choice)
            fh.close()
            value = 'Yes'
        except FileNotFoundError:
            print('filen finns inte')

        return value

    def handle_search_word(self):
        """
            return print if user input is in wordlist
        """
        word = input("search for: ")

        if self.d.search_word(word.lower().strip()):
            print('ordet: {} fanns i ordlistan!'.format(word))
        else:
            print('ordet: {} fanns inte!'.format(word))

    def handle_start_with(self):
        """
            return 10 words starts with prefix
            prefix = user input
        """
        prefix = input("search for: ")

        while self.d.search_word(prefix.lower().strip()):


    def handle_input(self, choice):
        """handle user choice from menu"""

        if choice == "1":
            self.handle_search_word()

        elif choice == "2":
            self.handle_start_with()

        elif choice == "3":
            print("du valde 3 - välj vilken fil du vill lägga till")
            self.set_new_dict(input("Vilken fil: "))
            # self.set_new_dict("words.txt")

        elif choice == "4":
            print("du ville skriva ut: \n")
            print(self.d.print_nodes())

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
