import random
roll = random.randint(1, 100)
tries = 0
def guess_rand(roll, tries):
    guess = input("Guess what the house rolled, between 1 - 100: ")
    tries += 1
    if guess.isdigit():
        guess = int(guess)
        if guess > 100:
            print("too high, please input a Number between 1 - 100")
            guess_rand(roll, tries)
        elif guess <= 0:
            print("too low, please input a Number between 1 - 100")
            guess_rand(roll, tries)
        else:
            comparator(guess, roll, tries)
    else:
        print("please input only Numbers between 1 - 100")
        guess_rand(roll, tries)

# comparator function compares users validated integer against random number generated
def comparator(guess, roll, tries):
    if guess == roll:
        tries_funct(tries)
    elif guess < roll:
        print("you guessed too LOW, try again")
        guess_rand(roll, tries)
    elif guess > roll:
        print("you guessed too HIGH, try again")
        guess_rand(roll, tries)

def tries_funct(tries):
    # if less than/equal to 5 attempts
    if tries <= 5:
        # be impressed
        print("Wow! You guessed it in only", tries, "tries!")
    # if more than 5 but less/equal to 10 attempts
    elif tries <= 10:
        # semi-shame user
        print("Oof, it took you", tries, "attempts to get it right")
    # if more than 10 attempts
    else:
        # hard shame the user
        print("it seriously took you", tries, "guesses to get it right..")


def main():
    guess_rand(roll, tries)    
    
if __name__ == "__main__":
    main()