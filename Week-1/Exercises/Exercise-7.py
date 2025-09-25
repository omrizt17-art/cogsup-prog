"""
Have a look at the script called 'human-guess-a-number.py' (in the same folder as this one).

Your task is to invert it: You should think of a number between 1 and 100, and the computer 
should be programmed to keep guessing at it until it finds the number you are thinking of.

At every step, add comments reflecting the logic of what the particular line of code is (supposed 
to be) doing. 
"""
from random import randint

print("Think of a number between 1 and 100. I will try to guess it!")

low, high = 1, 100 #setting the range
guesses = []

while True: #while didnt break
    #computer makes a random guess within the allowed range
    guess = randint(low, high)

    #avoid repeating guesses
    if guess in guesses:
        continue
    guesses.append(guess)

    print(f"My guess is {guess}")

    feedback = input("Is it correct (c), too low (l), or too high (h)? ").lower() #gletting feedback from user on the guess, lower to deal with capital letters

    if feedback == "c":
        print(f"Yay! I found your number: {guess} in {len(guesses)} tries 🎉")
        break
    elif feedback == "l":
        low = guess + 1
    elif feedback == "h":
        high = guess - 1
    else:
        print("Please enter c (correct), l (too low), or h (too high).")