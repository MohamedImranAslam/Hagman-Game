import random
from hangman_art import stages,logo
from hangman_words import word_list
from replit import clear
print(logo)

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
print(f'Pssst, the solution is {chosen_word}.')

lives = 6


display = []
for _ in range(word_length):
  display.append("_")

end_game = False
while not end_game:
  guess = input("Guess a letter: ").lower()
  clear()
  if guess in display:
    print(f"You already guessed {guess}")
  for position in range(word_length):
    letter = chosen_word[position]
    if letter == guess:
      display[position] = guess
  if guess not in chosen_word:
    lives -=1
    print(f"You guessed {guess},thats not in the word.You lose a life")
    print(stages[lives])
    if lives == 0:
      end_game=True
      print("You lose")
  print(f"{' '.join(display)}")
  if "_" not in display:
    end_game=True
    print("You Win")