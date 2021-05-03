from art import logo
import random

print(logo)

NUMBERS = list(range(1, 101))
LIVES = 5
ANSWER = random.choice(NUMBERS)


def guess_number(lives):
  if lives == 0:
    print(f"The answer was {ANSWER}. GAME OVER")
    return
  guess = int(input("Guess a number from 1 to 100:  "))
  if guess == ANSWER:
      print(f"The answer was {ANSWER}. Congrats!")
      return 
  if guess > ANSWER:
    lives -= 1
    print(f"Too high. You have {lives} lives left.")
    guess_number(lives)
  if guess < ANSWER:
    lives -= 1
    print(f"Too low. You have {lives} lives left.")
    guess_number(lives)
  
def play_game():
  if input("Do you want to play on 'hard' mode or 'easy' mode?'  ") == "easy":
    player_lives = LIVES + 5
  else: 
    player_lives = LIVES
  guess_number(player_lives)
play_game()

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

