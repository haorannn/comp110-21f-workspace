"""This program is aimed to judge the relationships between two numbers that you typed in."""

__author__ = "730490705"

left: str = input("Left-hand side: ")
right: str = input("Right-hand side: ")

judge_1: str = str(int(left) < int(right))
judge_2: str = str(int(left) >= int(right))
judge_3: str = str(int(left) == int(right))
judge_4: str = str(int(left) != int(right))
print(left + " < " + right + " is " + judge_1)
print(left + " >= " + right + " is " + judge_2)
print(left + " == " + right + " is " + judge_3)
print(left + " != " + right + " is " + judge_4)