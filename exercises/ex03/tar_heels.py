"""An exercise in remainders and boolean logic."""

__author__ = "730490705"


# Begin your solution here...
num_enter: int = int(input("Enter an int: "))
if num_enter % 2 == 0 and num_enter % 7 != 0: 
    print("TAR")
elif num_enter % 7 == 0 and num_enter % 2 != 0: 
    print("HEELS")
elif num_enter % 7 == 0 and num_enter % 2 == 0: 
    print("TAR HEELS")
else: 
    print("CAROLINA")