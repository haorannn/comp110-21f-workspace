"""Finding duplicate letters in a word."""

__author__ = "730490705"
word_enter: str = input("Enter a word: ")
judge: bool = False
i: int = 0
p: int = 0
while i < len(word_enter): 
    judge_letter = word_enter[i]
    p = i + 1
    while p < len(word_enter): 
        next_letter = word_enter[p]
        if judge_letter == next_letter:
            judge = True
        p += 1
    i += 1

print(f'Found duplicate: {judge}')
