#! usr/local/bin/env python3
"""
    Spellchecker classobject as main function for
    wordprogram.
    Kmom10 2019
"""
from trie import Trie

from error import NoRead #read file
from error import NoContent #content empty
from error import SearchError #unable to search
from error import EmptyTree #tree is empty
from error import SomethingWrong #error error


class SpellChecker():
    """main object for spellchecker"""

    def __init__(self):
        """constructor for SpellChecker()"""
        self.d = Trie()
        self.count = 0

    def get_count(self):
        """return count"""
        return self.count

    def start(self):
        """
            default start with textfile
            words.txt
        """

        try:
            self.set_new_dict("words.txt")
        except NoContent:
            print('Att: no content in dictionary')
        self.show_menu()


    def handle_search_word(self, word):
        """
            MENU 1. SEARCH WORD
            call for: bool TRIE.search_word()
            catch SearchError: nothing to search for
        """

        try:
            if len(word) >= 1:
                if self.d.search_word(word.lower().strip()):
                    print('your word "{}"" is in the dictionary.'.format(word))
                else:
                    print('could not find your word "{}"'.format(word))
            else:
                raise SearchError
        except KeyError:
            print("> no words in dictionary")
        # except SomethingWrong:
        #     print('something went wrong with handle_search_word()')

    def handle_start_with(self, prefix):
        """
            MENU 2. SEARCH WORDS WITH PREFIX
            prefix: user input
            return: a list of 10 words
        """

            # words = self.d.start_with(prefix.lower().strip())

        try:
            if prefix[-4:] == "quit":
                return False

            words = self.d.start_with(prefix.lower().strip())

            print('\nsearch result, words starting with "{}"'.\
                      format(prefix.upper() + '(max 10 words)'))
            for word in words:
                print(word)
            return True

        except SearchError:
            print('there are no words starting with  "{}"'.\
                format(prefix.upper()))
            return False

        except KeyError:
            print('could not search for "{}"'.\
                  format(prefix.upper())
                  + 'there are no words in the dictionary.')

            return False

    def handle_set_new_dict(self):
        """
             MENU 3. CHANGE DICTIONARY
             choice = user input - filename
        """
        print("Enter the filename:")
        print("Available are: dictionary.txt and tiny_dictionary.txt")

        try:
            filename = input("enter the name: ")
            self.set_new_dict(filename)
            print('> your file was uploaded succefully. With {} of words'.\
                format(self.get_count()))

        except NoRead:
            print('> could not read the file {}'.format(filename))

        except NoContent:
            print('> there where no content in your file {}'.format(filename))

    def set_new_dict(self, filename):
        """
            MENU 3. CHANGE DICTIONARY
            filename = user input - filename
        """
        self.d = None
        self.d = Trie()


        content = self._read_file(filename) #get content
        if content:
            words = content.split("\n") #skapar en lista med ord
            for word in words:
                # print('new word: {}'.format(word))
                self.d.add(word)
                self.count += 1
        else:
            raise NoContent

    @staticmethod
    def _read_file(filename):
        """
            private method read file
        """

        content = SpellChecker._open_file(filename)
        if content:
            fh = open(filename)
            content = fh.read().strip() #läser innehåll utan whitespace
            fh.close()
            return content
        else:
            raise NoRead

    @staticmethod
    def _open_file(filename):
        """
            open file. nothing else.
        """
        try:
            fh = open(filename)
            fh.close()
            return True
        except FileNotFoundError:
            print('could not open file. file not found.')

        return False

    def handle_print(self):
        """
            MENU 4. PRINT ALL WORDS
            Print: list of all words.
        """
        try:
            words_to_print = self.d.print_nodes()

            print("PRINT: \n")
            for word in words_to_print:
                print(word)
        except EmptyTree:
            print("The dictionary is empty.")

    def handle_input(self, choice):
        """
            handle user choice from menu
        """

        if choice == "1":
            try:
                word = input("search for: ")
                self.handle_search_word(word)
            except SearchError:
                print("> can't search for nothing")
        elif choice == "2":
            prefix = ""
            while True:

                prefix = prefix + input("search for: " + prefix)

                if not self.handle_start_with(prefix):
                    break

        elif choice == "3":
            self.handle_set_new_dict()

        elif choice == "4":
            self.handle_print()

        elif choice == "t":
            print(self.d.j_t())

        elif choice is None:
            print("invalid choice")
        else:
            raise SomethingWrong


    def show_menu(self):
        """eternity loop to show menu"""
        while True:
            try:
                print("--------------------------\n"
                      + "1) check if word is in dictionary\n"
                      + "2) get a suggestion of word. \n"
                      + "3) change dictionary. \n"
                      + "4) print all words in dictionary. \n"
                      + "q) quit.\n")

                choice = (input("-->  ")).strip()
                if choice == "q":
                    break
                elif choice is None:
                    print("please enter your choice")
                    continue
                else:
                    self.handle_input(choice)
            except SomethingWrong:
                print('please choose something from the menu')
                continue

if __name__ == '__main__':
    nytt = SpellChecker()
    nytt.start()
# nytt.show_menu()
