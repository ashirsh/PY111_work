"""
You can do it either with networkx ('cause tree is a graph)
or with dicts (smth like {'key': 0, value: 123, 'left': {...}, 'right':{...}})
"""

from typing import Any, Optional, Tuple
# import networkx as nx

binary_tree = {}


def insert(key: int, value: Any) -> None:
    """
    Insert (key, value) pair to binary search tree

    :param key: key from pair (key is used for positioning node in the tree)
    :param value: value associated with key
    :return: None
    """
    def insert_rec(tree):
        if tree:
            subtree = tree['left'] if key < tree['key'] else tree['right']
            insert_rec(subtree)
        else:
            tree['key'] = key
            tree['value'] = value
            tree['left'] = {}
            tree['right'] = {}

    if not binary_tree:
        binary_tree['key'] = key
        binary_tree['value'] = value
        binary_tree['left'] = {}
        binary_tree['right'] = {}
    else:
        insert_rec(binary_tree)

    return None


def remove(key: int) -> Optional[Tuple[int, Any]]:
    """
    Remove key and associated value from the BST if exists

    :param key: key to be removed
    :return: deleted (key, value) pair or None
    """
    def find_rec(tree):
        if tree:
            if tree['key'] == key:
                return [tree['key'], tree['value']]
            elif tree['key'] > key:
                return find_rec(tree['left'])
            elif tree['key'] < key:
                return find_rec(tree['right'])

    if binary_tree:
        return find_rec(binary_tree)


def find(key: int) -> Optional[Any]:
    """
    Find value by given key in the BST

    :param key: key for search in the BST
    :return: value associated with the corresponding key
    """
    def find_rec(tree):
        if tree['key'] == key:
            return tree['value']
        elif tree['key'] > key:
            return find_rec(tree['left'])
        elif tree['key'] < key:
            return find_rec(tree['right'])

    if binary_tree:
        return find_rec(binary_tree)

    return None


def clear() -> None:
    """
    Clear the tree

    :return: None
    """
    binary_tree.clear()
    return None


if __name__ == '__main__':
    print(binary_tree)
    insert(0, 42)
    insert(1, 99)
    insert(2, 1)
    print(binary_tree)
    print(find(2))
    print(remove(1))
