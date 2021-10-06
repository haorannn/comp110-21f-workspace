"""List utility functions part 2."""

__author__ = "730490705"

# Define your functions below


def only_evens(xs: list[int]) -> list[int]: 
    """This function returns the even numbers."""
    even_list: list[int] = []
    i: int = 0
    while i < len(xs): 
        if xs[i] % 2 == 0: 
            even_list.append(xs[i])
        i += 1
    return even_list


def sub(a_list: list[int], start_i: int, end_i: int) -> list[int]: 
    """This function returns a part of it."""
    sup_list: list[int] = []
    if start_i < 0: 
        start_i = 0
    
    if end_i > len(a_list): 
        end_i = len(a_list)

    if len(a_list) == 0: 
        sup_list = []

    while start_i < end_i: 
        sup_list.append(a_list[start_i])
        start_i += 1

    return sup_list


def concat(list1: list[int], list2: list[int]) -> list[int]:
    """This function returns the combined list1 and list2."""
    dup_list1: list[int]
    dup_list1 = list1
    dup_list2: list[int]
    dup_list2 = list2
    merge_list: list[int] = []
    i: int = 0
    while i < len(dup_list1): 
        merge_list.append(dup_list1[i])
        i += 1
    o: int = 0
    while o < len(dup_list2): 
        merge_list.append(dup_list2[o])
        o += 1
    return merge_list
