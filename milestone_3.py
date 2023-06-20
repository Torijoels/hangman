import random


def check_guess (self):
    guess = input ('Enter a single letter')
    guess_lower = guess.lower()
    word_list = ['orange', 'mango', 'banana', 'pear', 'tangerine']

    random.choice (word_list)
    word = random.choice (word_list)
    if guess in word:
       print (f"Good guess! {guess} is in the word.")
    else:
       print (f"Sorry, {guess} is not in the word. Try again.")


def ask_for_input ():
    while True:
        guess = input('guess a letter: ')
        if len(guess) == 1 and guess.isalpha():
             print ("Good guess!")
             break
        else:
             print ("Invalid letter. Please, enter a single alphabetical character.") 
             
    

   





if guess in self.word:
            print ("Good guess! {} is in the word.".format(guess))
            for letter in word:
                if letter in self.word_guessed:
                    print(f"letter", end="")
                elif:
                    print (f"_", end="")
                    self.num_letters -= 1
                else:
                print ("Sorry, {letter} is not in the word. Try again.")
                self.num_lives -= 1
                print ("You have {num_lives} lives left.")
