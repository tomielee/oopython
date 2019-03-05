#! usr/local/bin/env python3
"""
    Object unordered list
    Copied from https://dbwebb.se/kunskap/sorteringsalgoritmer#insertion-sort
    to kmmom05, assignment 2
"""
from error import NoValue
from error import WrongType


def insertion_sort(n):
    """ Insertion sort
        n =  linked list of object UnsortedList
    """

    for i in range(1, n.size()):
        j = i
        print('i: {} av size: {}'.format(i, n.size()))

        while j > 0 and n.get(j) < n.get(j-1):
            tmp = n.get(j)
            n.set(n.get(j-1), j)
            n.set(tmp, j-1)
            j -= 1

    return n.print_list()

def check_value_in_list(n):
    """return true if there is values in n"""
    if n:
        return True
    else:
        raise NoValue

def bubble_sort(n):
    """ Bubble sort
        n =  linked list of object UnsortedList
    """


    if check_value_in_list(n):
        for i in range(n.size()):
            for j in range(n.size()-1-i):
                if n.get(j) > n.get(j+1):
                    tmp = n.get(j)
                    n.set(n.get(j+1), j)
                    n.set(tmp, j+1)
                else:
                    raise WrongType

    return n.print_list()

    # for i in range(len(items)):
    #     for j in range(len(items)-1-i):
    #         if items[j] > items[j+1]:
    #             items[j], items[j+1] = items[j+1], items[j]     # Byt plats
    #
    # return items
