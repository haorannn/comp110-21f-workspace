"""This is a small game."""
__author__ = "730490705"
import random
NAMED_CONSTANT: str = "\U0001F604"
points: int
player: str


def main() -> None: 
    """The main function of this game."""
    choice: str = input("Type in \"Play\" to play the game and \"end\" to end the game.")
    while choice == "Play": 
        global points
        points: int
        greet()
        options()
    

def greet() -> None: 
    """This is the greet function that gets your name."""
    global player
    name: str = input("What is your name? ")
    player = name
    print(f"Generating random numners and asking the users to guess whether the numbers are evenly divisible by 7 and count correct points that they guess{NAMED_CONSTANT}. ")
    print("If your guess is correct, then you will have 1 points. If your guess is incorrect. then your points remain the same. ")
    

def options() -> None: 
    """This function provides the different options."""
    print("Option 1 starts the game, option 2 is an mysterious option, and option 3 ends the game. ")
    option_num: int = int(input("Please enter your options: 1 or 2 or 3: "))
    if option_num == 1: 
        print(f"You will start the game! Good luck!{NAMED_CONSTANT}")
        option_one()
    elif option_num == 2: 
        print("Ohhhh! You got an extra point! ")
        option_two()
    elif option_num == 3: 
        print("It's time to say goodbye. ")
        option_three()


def option_one() -> None: 
    """This is the option one, and you can play this game in this function."""
    global points
    lower: int = int(input("Please enter the lower bound in an integer: "))
    upper: int = int(input("Please enter the upper bound in an interger: "))
    num: int = random_num_generator(lower, upper + 1)
    judge_entered = bool(input("Please enter \"True\" or \"False\" to judge whether the random-generated number is evenly divisible by 7. "))
    if judge_entered is True and num % 7 == 0: 
        points += 1
        print("Congratulations! You got it right! ")
    else: 
        points += 0
        print("Opps, you did not get it correct. ")
    option_three()


def option_two() -> None: 
    """This mysterious option can offer players an extra point."""
    global points
    points += 1
    options()


def option_three() -> None: 
    """This function ends the gaming process."""
    global points
    global player
    comments: str = ""
    comments += f"{player} is an awesome player!"
    print(f"{player} got {points} on this game.")


def random_num_generator(lower_bound: int, upper_bound: int) -> int: 
    """This function provides a random number."""
    random_num: int = random.randint(lower_bound, upper_bound + 1)
    return random_num


if __name__ == "__main__":
    main()