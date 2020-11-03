import random
import math

class difficulty:
    def __init__(self, lower, higher, guesses=math.inf, name=None):
        self.lower = lower
        self.higher = higher
        self.guesses = guesses
        if name is None:
            self.name = "Custom difficulty #" + str(len(difficulties) + 1)
        else:
            self.name = name

difficulties = [
    difficulty(1, 50, name="Practice 50"),
    difficulty(1, 100, name="Practice 100"),
    difficulty(1, 500, name="Practice 500"),
    difficulty(1, 50, 12, name="Easy 50"),
    difficulty(1, 50, 8, name="Medium 50"),
    difficulty(1, 50, 6, name="Hard 50"),
    difficulty(1, 100, 12, name="Easy 100"),
    difficulty(1, 100, 8, name="Medium 100"),
    difficulty(1, 100, 6, name="Hard 100"),
    difficulty(1, 500, 12, name="Easy 500"),
    difficulty(1, 500, 8, name="Medium 500"),
    difficulty(1, 500, 6, name="Hard 500"),
]
selected_difficulty = difficulties[0]
current_guesses = 0
number = None

resp = None
resp_val = True

print("Welcome!")
while True:
    print(
        """
        
        Please select from the following:
        
        1: Play game
        2: Edit difficulties
        
        """)

    resp = input("")

    if str.strip(resp) == "1":
        print("Select difficulty:")
        i = 0
        while i < len(difficulties) - 1:
            print(f"{str(i + 1)}: {difficulties[i].name}")
            i += 1
        while True:
            resp = input()
            try:
                selected_difficulty = difficulties[int(resp) - 1]
                break
            except:
                resp_val = False
                print("Invalid input, please enter a number for available difficulties")
        current_guesses = 0
        number = random.randint(selected_difficulty.lower, selected_difficulty.higher)
        while True:
            guess = input(f"Enter a number between {selected_difficulty.lower} and {selected_difficulty.higher}\n")
            if str.isnumeric(guess):
                if number < int(guess) > selected_difficulty.lower:
                    print("Lower")
                    current_guesses += 1
                elif number > int(guess) and int(guess) < selected_difficulty.higher:
                    print("Higher")
                    current_guesses += 1
                elif str(number) == guess:
                    current_guesses += 1
                    suff = "!"
                    if selected_difficulty.guesses != math.inf:
                        suff = "(with " + str(selected_difficulty.guesses - current_guesses) + " remaining!)"
                    print(f"You won! You guessed the correct number({number}), in {current_guesses} guesses" + suff)
                    break
                else:
                    print("Invalid guess, please make sure your guess is in the right range.")
            elif guess == "cheat":
                print("The number is " + str(number))
            else:
                print("Invalid input, please enter a number.")
    elif str.strip(resp) == "2":
        print("N/A")
        print("Please enter a lower number for the range")
        tempL = input("")
        print("Please enter a higher number for the range")
        tempH = input("")
        print("Please enter a guess limit for difficulty(optional, press enter to skip)")
        tempG = input("")
        if str.strip(tempG) == "" or tempG == 0 or not str.isnumeric(tempG):
            tempG = "NA"
        print("Please enter a name for the difficulty(optional, press enter to skip)")
        tempN = input("")
        if str.strip(tempN) == "":
            tempN = "Custom Difficulty " + str(len(difficulties) - 11)
        displayguesses = "Guesses: Unlimited"
        if tempG != "NA":
            displayguesses = "Guesses: " + str(tempG)
        print(f"{tempN}\n  Lower: {str(tempL)}  Higher: {str(tempH)}  \n  {displayguesses}\n  ")
        print("Confirm: Please enter 'Y' or 'N'.")
        if str.capitalize(input("")) == "Y":
            if tempG == "NA":
                difficulties.append(difficulty(tempL, tempH, name=tempN))
            else:
                difficulties.append(difficulty(tempL, tempH, float(tempG), tempN))
