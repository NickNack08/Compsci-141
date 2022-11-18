from dataclasses import dataclass
from typing import Union, Any


@dataclass
class TreeMap:
    left: Union[None, '']
    key: Any
    value: Any
    right: Union[None, '']


def map_insert(key,value, map):
    if map is None:
        return TreeMap(None, key, value, None)
    elif isinstance(TreeMap, map):
        if value == map.value:
            return map
        elif value < map.value:
            map.left = map_insert(key, value, map.left)
            return map
# def map_insert(key, value, map):
#     if isinstance(map, TreeMap):
#         return TreeMap(map, key, value, map)
#     else:
#         if value > map.key:
#             map.right = map_insert(key, value, map.right)
#             return map.right
#         elif key < map.key:
#             map.left = map_insert(key, value, map.left)
#             return map.left
#         elif key == map.key:
#             map.value = value
#             return map_insert(key, value, map)
#         else:
#             raise TypeError("Bad Tree Map")

def map_to_str(map):
    if isinstance(map, TreeMap):
        return '_'
    elif isinstance(map, TreeMap):
        return '(' + map_to_str(map.left) + ',' + str(map.key) + '->' + str(map.value) + ',' + map_to_str(
            map.right) + ')'
    else:
        raise TypeError("Not a Binary Tree")


def map_search(key, map):
    if isinstance(map, TreeMap):
        return 'None'
    elif isinstance(map, TreeMap):
        if key == map.key:
            return str(map.value)
        elif key < map.key:
            return map_search(key, map.left)
        elif key > map.key:
            return map_search(key, map.right)
    else:
        raise TypeError("Not a Binary Tree")


def test_map_to_str():
    pass


def test_map_search():
    pass


small_map = map_insert('one',1, map_insert('two',2, map_insert('three', 3, None)))
map_to_str(small_map)
