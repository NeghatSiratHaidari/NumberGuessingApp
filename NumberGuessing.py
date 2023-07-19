import random

difficulty = int(input("Choose the difficulty (1 = Easy, 2 = Medium, 3 = Hard, 4 = Legendary): "))
highest_val = 0
lowest_val = 1
if difficulty == 1:
    highest_val = 10
elif difficulty == 2:
    highest_val = 100
elif difficulty == 3:
    highest_val = 500
elif difficulty == 4:
    highest_val = 1000
else:
    print(difficulty, "is not an option")
    exit(0)

rand_int = random.randint(lowest_val, highest_val)
guess = 0
guess_str = "Guess the number. It shoud be a number between (1, " + str(highest_val) + "). Type 0 to quit: "
while True:
    guess = int(input(guess_str))
    if guess == 0:
        break
    elif guess < lowest_val:
        print("Don't use negative integers.")
        exit(0)
    elif guess == rand_int:
        print("You guessed the right number!!!")
        break
    elif guess < rand_int:
        guess_str = "Guess higher: "
        continue
    elif guess > rand_int and guess <= highest_val:
        guess_str = "Guess lower: "
        continue
    else:
        print("It must be between 1 and ", highest_val, '.')
        continue
