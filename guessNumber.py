import random
roll = random.randint(1, 100)
tries = 0
"""
    PARAM(Roll): The random number between 1 and 100
    PARAM(tries): the number of attempts the user has made
        This function validates the user input ensuring only integers between 1 and 100 are submitted
        when criteria is met, this function calls Comparator function to compare user input against
        the random roll. 
"""
def guess_rand(roll, tries):
    # get user's guess between 1 and 100
    guess = input("Guess what the house rolled, between 1 - 100: ")
    # tries - Count the users attempts at guessing the roll
    tries += 1
    # if User input is a number
    if guess.isdigit():
        # Convert user input to a Integer
        guess = int(guess)
        # If user input is greater than 100 throw error
        if guess > 100:
            print("too high, please input a Number between 1 - 100")
            # Call function to allow user to re-attempt
            guess_rand(roll, tries)
        # If user input is less than 0 throw error
        elif guess <= 0:
            print("too low, please input a Number between 1 - 100")
            # Call function to allow user to re-attempt
            guess_rand(roll, tries)
        else:
            # if user input meets required criteria call Comparator function - passing users input, the random roll value, and their number of attempts 
            comparator(guess, roll, tries)
    # If user input is not a number throw error
    else:
        print("please input only Numbers between 1 - 100")
        # Call function to allow user to re-attempt
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