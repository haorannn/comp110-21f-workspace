"""List utility functions."""

__author__ = "730490705"
# TODO: Implement your functions here.


def all(a: list[int], b: int) -> bool:
    """This function is to judge whether b is in a."""
    i = 0
    judge = False
    while i < len(a): 
        judge_item: int = a[i]
        if judge_item == b: 
            judge = True
            i += 1
        elif judge_item != b: 
            judge = False
            break
    return judge


def is_equal(list1: list[int], list2: list[int]) -> bool: 
    """This function is to judge whether two lists are the same."""
    judge: bool = False
    if len(list1) == len(list2): 
        i: int = 0
        if len(list1) == len(list2) == 0: 
            judge = True
        elif len(list1) > 0 and len(list2) > 0: 
            while i < len(list1): 
                if list1[i] == list2[i]: 
                    i += 1
                elif list1[i] != list2[i]: 
                    return False
                return True
    elif len(list1) != len(list2): 
        judge = False
    
    return judge


def max(int_li: list[int]) -> int: 
    """This function will select the largest number in list."""
    if len(int_li) == 0: 
        raise ValueError("max() arg is an empty List")
    elif len(int_li) != 0: 
        max_int: int = int_li[0]
        i: int = 0
        while i < len(int_li): 
            if int_li[i] > max_int: 
                max_int = int_li[i]
                i += 1
            elif int_li[i] <= max_int: 
                max_int += 0
                i += 1
    return max_int