
import random

secret = random.randint(1, 10)

print("Guess the number (1–10):")
while True:
    guess = int(input("Your guess: "))
    if guess < secret:
        print("Too low")
    elif guess > secret:
        print("Too high")
    else:
        print("Correct! The number was", secret)
        break
