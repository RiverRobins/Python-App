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

difficulties = [difficulty(1, 50), difficulty()]

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

    print("Please enter a lower number for the range")
    print("Please enter a lower number for the range")


