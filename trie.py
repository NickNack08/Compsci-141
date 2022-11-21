"""
file: treemap.py
author: Nick Duggan nkd2840@rit.edu
assignment: homework 12
date: 11/18/22
description: treemap.py is a module used to create a tree map, insert key value pairs,
convert the tree map to a string, and search for a value based on a provided key.
Included are test functions with several instances of treemaps.
"""


"""You could make the trie to list function sort the values first and then insert them """

from dataclasses import dataclass
from typing import Union, Any

@dataclass
class Trie:
    left: Union[None, 'Trie']
    value: Any
    right: Union[None, 'Trie']

def split(x, trie, idx):
    node = Trie(None, "", None)
    if trie.value[idx] == '0' and x[idx] == '0':
        node.left = split(x, trie, idx + 1)
    elif trie.value[idx] == '1' and x[idx] == '1':
        node.right = split(x, trie, idx + 1)
    elif trie.value[idx] == '1' and x[idx] == '0':
        node.left = Trie(None, x, None)
        node.right = trie
    else:
        node.right = Trie(None, x, None)
        node.left = trie
    return node


def insert(trie, st, idx=0):
    if trie is None:
        return Trie(None, st, None)
    elif trie.value == "":
        if st[idx] == '0':
            trie.left = insert(trie.left, st, idx + 1)
        elif st[idx] == '1':
            trie.right = insert(trie.right, st, idx + 1)
        return trie
    else:
        return split(st, trie, idx + 1)


def test():
    test_trie = insert(insert(insert(insert(insert(None, '001010'), '000111'), '111000'), '010000'), '110001')
    print(trie_to_list(test_trie))
    print(largest(test_trie))
    print(smallest(test_trie))
    print(size1(test_trie))
    print(height(test_trie, 0))

def trie_to_list(trie):
    return trie_to_list_helper(trie, [])


def trie_to_list_helper(trie, trie_list):
    if trie is not None:
        if trie.left is None and trie.right is None:
            trie_list += [trie.value]
        trie_to_list_helper(trie.left, trie_list)
        trie_to_list_helper(trie.right, trie_list)
    return trie_list


def largest(trie):
    if trie is not None:
        if trie.left is None and trie.right is None:
            return trie.value
        return largest(trie.right)


def smallest(trie):
    if trie is not None:
        if trie.left is None and trie.right is None:
            return trie.value
        return smallest(trie.left)

def search(trie, st):
    pass


def size1(trie):
    return size(trie, 0)
def size(trie, count):
    if trie is not None:
        if trie.left is None and trie.right is None:
            count += 1
        size(trie.left, count)
        size(trie.right, count)
    return count

def height(trie, count):
    if trie is not None:
        if trie.left == "":
            height(trie.left, count + 1)
        elif trie.right == "":
            height(trie.right, count + 1)
        elif trie.left is None and trie.right is None:
            return count
    #     count = 0
    #     while trie.left is not None and trie.right is not None:
    #         if trie.left == "":
    #             count += 1
    #             trie = trie.left
    #             continue
    #         if trie.right == "":
    #             count += 1
    #             trie = trie.right
    #             continue
    #     return count


test()



"when you search, we want to find the biggest one in the left side subtree," \
" or the smallest value in the right subtree"



