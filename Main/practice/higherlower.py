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
    difficulty(1, 50, name="Practice 500"),
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
            print(str(i + 1), difficulties[i])
            i += 1
        while True:
            resp = input()
            try:
                selected_difficulty = difficulties[int(resp)]
                break
            except:
                resp_val = False
                print("Invalid input, please enter a number for available difficulties")
        current_guesses = 0
        number = random.randint(selected_difficulty.lower, selected_difficulty.higher)
        while True:
            guess = input(f"Enter a number between {selected_difficulty.lower} and {selected_difficulty.higher}")

            if number > int(guess) > selected_difficulty.lower:
                print("Lower")
                current_guesses += 1
            elif number < int(guess) < selected_difficulty.higher:
                print("Higher")
                current_guesses += 1
            elif number == guess:
                suff = "!"
                if selected_difficulty.guesses != math.inf:
                    suff = " with" + str(selected_difficulty.guesses - current_guesses) + " remaining!"
                print(f"You won! You guessed the correct number({number}), in {current_guesses}" + suff)
                break
            else:
                print("Invalid guess, please make sure your guess is in the right range.")

    print("Please enter a lower number for the range")
    print("Please enter a lower number for the range")


