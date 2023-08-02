import random
import word_list
import ascii_art

play_again = "True"

while play_again == "True":
    print(ascii_art.hangman_ascii)

    lives = 6

    hangman_word = ""

    chosen_word = random.choice(word_list.words)
    length = len(chosen_word)

    for i in range(0,length):
        hangman_word = hangman_word + "-"

    print("The chosen word is",hangman_word)

    while lives > 0 and hangman_word != chosen_word:
        letter_user = input("Enter a letter you think is in the word: ").lower()
    
        if letter_user in hangman_word:
            print(f"You've already guessed {letter_user}")

        for i in range(0,length):
            if chosen_word[i] == letter_user:
                hangman_word = hangman_word[0:i] + letter_user + hangman_word[i+1:length]

        print(hangman_word)

        if hangman_word == chosen_word:
            print("You win!")

        if not letter_user in chosen_word:
            lives = lives - 1
            print(f"Letter {letter_user} is not in the word")
            print(ascii_art.stages[lives])

        if lives == 0:
            print("You lose")
            print(f"The answer was {chosen_word}")
        
        if lives == 0 or hangman_word == chosen_word:
            playagain_choice = input("Play again?: ").lower()
        
            if playagain_choice == "yes":
                print("")
            elif playagain_choice == "no":
                print("Goodbye!")
                play_again = "False"
            else:
                print("Guess that's a no")
                play_again = "False"