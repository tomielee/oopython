#! usr/local/bin/env python3
"""
    Assignment for kmom06 - oophython
    Create a binary search tree.
    Binary Search Tree class object.
"""

from node import Node

class BinarySearchTree():
    """
    class object that works like a binary search tree
    root = parent. child < root = left.child, child > root = right.child
    """

    def __init__(self):
        """constructor for BST"""
        # __init__: Skapa ett objekt, sätt root till None.

        self.root = None
        self.size = 0


    def insert(self, key, value):
        """insert nodes (a value at a key position) to BST"""
        # insert: Skapar en ny nod med key och value,
        # lägger till en noden på rätt plats i trädet, baserat på key.
        if self.root is None:
            self.root = Node(key, value)
        else:
            self._insert(key, value, self.root)



    @staticmethod
    def _insert(key, value, node):
        """private insert method to insert values."""
        # https://dbwebb.se/guide/kom-igang-med-objektorienterad-programmering-i-python/statiska_metoder#statiskmetod

        if key < node: #works only with __lt__ in Node
            if node.has_left_child():
                BinarySearchTree._insert(key, value, node.left)
            else:
                node.left = Node(key, value, node)
        elif key > node:
            if node.has_right_child():
                #om noden har ett barn till höger - kallar på instansen
                #igen där den höra noden blir vår "nya root/parent"
                BinarySearchTree._insert(key, value, node.right)
            else:
                #om noden inte har barn till höger. skapa en ny.
                node.right = Node(key, value, node)
        else:
            #om nyckeln reda finns så ska värdet bytas ut.
            node.value = value


    def inorder_traversal_print(self):
        """print nodes in order"""
        # inorder_traversal_print: Skriver ut en noderna i trädet i rätt
        # ordning, lågt till högt.

        self._print_nodes(self.root)


    @staticmethod
    def _print_nodes(node):
        """private method to print the nodes"""
        # in order kräver både left och right för att veta vad som är in.
        # left och right behöver kollas separat!!!
        if node.has_left_child():
            BinarySearchTree._print_nodes(node.left)

        # utskriften för inorder - efter left men innan right
        print(node.value)

        if node.has_right_child():
            BinarySearchTree._print_nodes(node.right)

    def get(self, key):
        """ return value at index key """
        # get: Returnera value från noden med nyckeln key.
        # Om key inte finns i trädet lyft ett KeyError exception (det inbyggda).
        if self.root is None:
            raise KeyError
        else:
            return self._get(key, self.root).value

    @staticmethod
    def _get(key, node):
        """ return node, at key"""
        #GLÖM INTE att returnera värdet så att det kommer med alla
        #nivåer till key == node

        if node is None:
            raise KeyError

        if key == node:
            return node
        elif key < node:
            return BinarySearchTree._get(key, node.left)
        elif key > node:
            return BinarySearchTree._get(key, node.right)




    def remove(self, key):
        """remove node"""
        # remove: Ta bort nod med samma key.
        # Om nod med key inte finns lyft KeyError exception (det inbyggda).

        if self.root is None:
            raise KeyError
        else:
            #1. get the node to remove.
            node_to_remove = BinarySearchTree._get(key, self.root)

            #this is the node_to:removes content..
            print('\nnode to remove K: {} V {}'.\
            format(node_to_remove.value, node_to_remove.key))

            #2. rearrange stuff. but the value should be the same
            returned_node = self._remove_value(node_to_remove)

            #this is the returned nodes value
            print('\nreturned value: {}'.format(returned_node))

            return returned_node


    def _remove_value(self, node):
        """remove node at key"""

        node_to_return = node.value
        print('\nold node K: {} V {}'.format(node.value, node.key))
        if node.is_leaf():
            #NO CHILDREN
            self.remove_node_is_leaf(node)

        elif node.has_both_children():
            #HAS TWO CHILDREN
            successor = BinarySearchTree._find_successor(node.right)
            node.key = successor.key
            node.value = successor.value

            if successor.is_left_child():
                successor.parent.left = successor.right
            else:
                successor.parent.right = successor.right

        elif node.has_left_child():
            # HAS LEFT CHILD
            self.remove_node_has_left_child(node)

        elif node.has_right_child():
            #HAS RIGHT CHILD
            self.remove_node_has_right_child(node)

        print('new node K: {} V {}'.format(node.value, node.key))
        return node_to_return

    def remove_node_is_leaf(self, node):
        """remove node that has no children"""
        if node == self.root:
            self.root = None
        elif node.is_left_child():
            node.parent.left = None
        else:
            node.parent.right = None

    def remove_node_has_left_child(self, node):
        """return node that has left child"""
        if node.has_parent():
            if node.is_left_child():
                node.parent.left = node.left
            else:
                node.parent.right = node.left
        else:
            self.root = node.left

    def remove_node_has_right_child(self, node):
        """return value of node that has right child """
        if node.has_parent():
            if node.is_left_child():
                node.parent.left = node.right
            else:
                node.parent.right = node.right
        else:
            self.root = node.right

    @staticmethod
    def _find_successor(successor):
        """return successor
        the node bigger than current node but smaller than nodes child.
        """
        if successor.left is None:
            return successor

        return BinarySearchTree._find_successor(successor.left)


bst = BinarySearchTree()


# 20, 15, 10, 18, 9, 11, 17, 19, 16

bst.insert(20, "tjugo")
bst.insert(15, "femton")

bst.insert(10, "tio")
bst.insert(18, "arton")

bst.insert(9, "nio")
bst.insert(11, "elva")
# bst.insert(17, "sjutton")
# bst.insert(19, "nitton")
#
# bst.insert(16, "sexton")

bst.inorder_traversal_print()
bst.remove(15)
bst.inorder_traversal_print()
