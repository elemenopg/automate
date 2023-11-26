import random

print("I am thinking of a number between 1 and 20.")
random_number = random.randint(1,20)
attempts = 0

while True:    
    guess = int(input("Take a guess.\n"))
    if guess == random_number:
        if attempts == 0:
            print("Good job! You guessed the number right the first time!")
        else:
            print(f'Good job! You guessed my number in {attempts} guesses!')
        break
    elif guess > random_number:
        attempts += 1
        print("Your guess is too high.")
        continue
    else:
        attempts += 1
        print("Your guess is too low.")
        continue