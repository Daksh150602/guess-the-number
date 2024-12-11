import random
import art
print(art.logo)
EASY_LEVEL_TURNS=10
HARD_LEVEL_TURNS=5
turns=0
def check_answer(user_guess,answer,turns):
    if user_guess>answer:
        print("TOO HIGH")
        return turns-1
    elif user_guess<answer:
        print("TOO LOW")
        return turns - 1
    else:
        print(f"you got it the answer is {answer}")

def choose_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard':").lower()
    if difficulty == "easy":
        return EASY_LEVEL_TURNS
    elif difficulty == "hard":
        return HARD_LEVEL_TURNS

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
number=random.randint(1,100)
turns=choose_difficulty()
guess=0
while guess != number:
    print(f"you have {turns} attempts remaining to guess the number")
    guess=int(input("Make a guess:"))
    turns=check_answer(guess,number,turns)
    if turns==0:
        print("you ran out of the guesses")



