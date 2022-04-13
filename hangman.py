import random

from words import words

import string

def get_valid_word(words):
    word = random.choice(words)  #randomly chooses something from the list
    while '-' in word or ' 'in word:
        word = random.choice(words)
    
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letter = set(word) #letter in the word
    alphabet = set(string.ascii_uppercase)
    used_letter = set() #what the user has guessed

    lives = 6
    #getting user input
    while len(word_letter)> 0 and lives > 0:
        #letter used
        #' '.join('a', 'b', 'cd') ---- 'a b cd'
        print('You habe', lives,'lives left and  You have used these letters: ',' '. join(used_letter))

        #what current word is(ie W - R D)
        word_list = [letter if letter in used_letter else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input ('Guess a letter: ').upper()
        if user_letter in alphabet - used_letter:
            used_letter.add(user_letter)
            if user_letter in word_letter:
                word_letter.remove(user_letter)

            else:
                lives = lives - 1 #take away alife if wrong
                print( 'Letter is not in word')

        elif user_letter in used_letter:
            print(' You have already used that letter. Please try algain.')

        else:
            print('Invalid character. Please try again.')

    #get here when len(word_letter) == 0
    if lives == 0:
        print('Sorry, you died. The word was ',word)
    else:
        print('You guessed the word', word , '!!')

print(hangman())
