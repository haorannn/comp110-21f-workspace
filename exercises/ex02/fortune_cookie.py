"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730490705"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint
# Begin your solution here...
print("Your fortune cookie says...")
num = randint(1, 4)
if num == 1: 
    print("You will be smart! ")
elif num == 2: 
    print("You will be healthy all the time! ")
elif num == 3: 
    print("You will have more meaningful life! ")
elif num == 4: 
    print("You will have a gift from people around you! ")
print("Now, go spread positive vibes!")