from art import logo
import random

def display_welcome():
    print(logo)
    print("Welcome to the number guessing game!")
    print("I'm thinking of a number between 1 and 100.")

        
def get_difficulty():
    while True:
        difficulty=input("Choose a difficulty.Type 'easy' or 'hard': ").lower()
        if difficulty in ['easy','hard']:
            return difficulty
        else:
            print("Please type either 'easy' or 'hard'")
        
def no_of_attempts(difficulty_level):
    attempts=0
    if difficulty_level=='easy':
        attempts=10
    else:
        attempts=5
    print(f"You have {attempts} attempts remaining to guess the number.")
    return attempts

def check_guess(guess,attempts,has_guessed_number,secret_number):
    if guess==secret_number:
        print(f"You got it! The answer was {secret_number}.")        
        return attempts,True   
    elif guess<secret_number:   
        attempts-=1
        print("Too low")
    else:
        attempts-=1
        print("Too high")
    
    if attempts==0:
        print("You've run out of guesses,you lose.")
        return attempts,True     
    
    print("Guess again")    
    print(f"You have {attempts} attempts remaining to guess the number.")    
    return attempts,has_guessed_number   

def play_game():
    display_welcome()
    difficulty=get_difficulty()
    attempts=no_of_attempts(difficulty)    
    secret_number=random.randint(1,100)
    has_guessed_number=False

    while not has_guessed_number:
        guess=int(input("Make a guess: "))
        
        attempts,has_guessed_number=check_guess(guess,attempts,has_guessed_number,secret_number)
        
            
            
play_game()