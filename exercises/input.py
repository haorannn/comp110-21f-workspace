"""List Exercises"""
__author__ = "730490705"

from random import randint

lists: list[int] = list()

while len(lists) == 0 or lists[len(lists) - 2] != 10: 
    lists.append(randint(1, 20))

lists.pop(len(lists) - 1)
print(lists)