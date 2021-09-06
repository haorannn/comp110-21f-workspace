"""Counting letters in a string."""
__author__ = "730490705"
# Begin your solution here...
ini_letter = str(input("What letter do you want to search for?: "))
word_enter = str(input("Enter a word: "))
word_len = int(len(word_enter))


sum = 0
i = 0
while i < word_len:
    if ini_letter == word_enter[i]: 
        sum += 1
    i += 1

print("Count: " + str(sum))