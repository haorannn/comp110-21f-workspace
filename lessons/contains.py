"""Practice implement a function using list."""


def contains(needle: str, haystack: list[str]) -> bool: 

    i: int = 0
    while i < len(haystack): 
        item: str = haystack[i]
        if item == needle: 
            return True
        i = i + 1
    return False


print(contains("John", ["Sarah", "Gavin"]))