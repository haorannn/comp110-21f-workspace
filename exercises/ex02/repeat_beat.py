"""Repeating a beat in a loop."""
__author__ = "730490705"
# Begin your solution here...
word = input("What beat do you want to repeat? ")
num = int(input("How many times do you want to repeat it? "))

while True: 
    if num > 0: 
        print(str(word + " ") * (num - 1) + word)
        break
    elif num <= 0: 
        print("No beat...")
        break