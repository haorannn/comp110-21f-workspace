"""Drawing forests in a loop."""

__author__ = "730490705"

# The string constant for the pine tree emoji
TREE: str = '\U0001F332'
tree_num: int = int(input("Depth: "))
p: int = 1
while p <= tree_num: 
    print(TREE * p)
    p += 1