import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

print(chosen_word)

lives = 6
display = []

for letters in range(len(chosen_word)):
    display += "_"

should_continue = True
while should_continue:
    guess = input("guess a letter: ").lower()

    if guess in display:
        print(f"You have already guessed {guess}")
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"you guessed {guess}, that is not in the word, you loose a life")
        lives -= 1
        if lives == 0:
            should_continue = False
            print("You loose")

    print(f"{' '.join(display)}")

    if "_" not in display:
        should_continue = False
        print("you win")
