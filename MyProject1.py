import random

guess_word = ["algorithm", "variable", "function", "debugger", "compiler", "framework", "interface", "database", "iteration", "encryption"]
word = random.choice(guess_word)

guessed_word = ['_'] * len(word)
attempts = 10
guessed_letters = [ ]

print('Welcome to the guessing game!')
print('Hint: The words are related to software and programming')

while attempts > 0:
    print('\nCurrent word: ' + ' '.join(guessed_word))
    guess = input('Can you please guess a letter or whole word?: ').lower()

    if guess == word:
        print(f"\n✨ Incredible! You guessed the word correctly: {word}")
        break

    elif len(guess) == 1 and guess.isalpha():
        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue

        guessed_letters.append(guess)


    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
        print('What a shot!')
    else:
        attempts -= 1
        print('Oh! Think again! Attempts left: ' + str(attempts))

    if '_' not in guessed_word:
        print('\nYeyy! You guessed the word!: ' + word)
        break

if attempts == 0 and '_' in guessed_word:
    print('\nYou\'ve run out of attempts! Sorry... The word was: ' + word)
