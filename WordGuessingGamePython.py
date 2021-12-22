# %%
#import stuff used
import random
from typing import cast
f = open("words_alpha.txt")
random_words = f.read().split()
f.close()
cycle = 0 #do i need this?
chosen_words = []

#score
won = 0
lost = 0

#make variables
success = False
guessed_letters = []
guessed_words = []

play = str(input("Want to guess a word?"))

while cycle < 100 and (play == "yes" or play == "Yes"):
    if play == "yes":
        word = random.choice(random_words)
        letters = list(word)
        if word in chosen_words:
            continue
        else:
            chosen_words.append(word)
            cycle += 1
            guesses = 7
            goal = list("_"*len(word))
        while guesses > 0 and not success: #the actual game starts
            guess = input("Guess a word or letter:")
            if len(guess) == 1 and guess.isalpha(): #guessing a letter
                if guess in guessed_letters:
                    print("You already tried that letter.")
                elif guess not in letters:
                    print("That letter is not in the word, try again.")
                    guesses -= 1
                    print(f"You have {guesses} guesses left.")
                    guessed_letters.append(guess)
                    print(f"You've guessed {guessed_letters}.")
                else:
                    for x in range(0, len(word)): #x is index number, loops through word length
                        if guess == word[x] and goal[x] == '_': #compare if guess is in word and the index place has a _
                            goal[x] = guess #then replace that place in goal with the guess
                        count = 0
                    for item in goal:
                        if (item == "_"):
                            count += 1
                    if count == 0:
                        won += 1
                        print(f"You've won! The word is {word}.")
                    print(goal)
                    print(guess + " is in the word, great job!")
                    print(f"You have {guesses} guesses left.")
                    guessed_letters.append(guess)
                    print(f"You've guessed {guessed_letters}.")
                
            elif len(guess) > 1 and guess.isalpha(): #guessing a word
                if guess in guessed_words:
                    print("You already guessed the word.")
                elif guess != word:
                    print("That's not the word, try again.")
                    guesses -= 1
                    print(f"You have {guesses} guesses left.")
                    guessed_words.append(guess)
                    print(f"You've guessed {guessed_words}.")
                else:
                    success = True 
            else:
                print("Please submit a letter or word.")
        if success:
            print("Congrats, you won!")
            won += 1
            print(f"You've won {won} times.")
            play = str(input("Want to play again?"))
        else:
            print("You ran out of guesses.")
            lost += 1
            print(f"You've lost {lost} times.")
            play = str(input("Want to play again?"))
    elif play == "no" or play == "No":
        break
    else:
        print("Please enter 'yes' or 'no'.")

# %%
