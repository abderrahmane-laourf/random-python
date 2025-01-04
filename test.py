import random

def guess_the_number():
    print("Welcome to 'Guess the Number' game!")
    print("I'm thinking of a number between 1 and 100.")
    
    # Generate a random number
    number_to_guess = random.randint(1, 100)
    attempts = 0
    
    while True:
        # Ask the user for their guess
        try:
            user_guess = int(input("Take a guess: "))
            attempts += 1
            
            if user_guess < number_to_guess:
                print("Too low! Try again.")
            elif user_guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid number.")

# Run the game
guess_the_number()