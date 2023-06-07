import random


class HangMan:
    def __init__(self, word_list, num_lives=5):
        self.word = random.choice (word_list)
        self.word_guessed = []
        self.num_letters = len(set(self.word_guessed))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []  

    def check_guess (self, guess):
         guess = input('guess a letter: ')
         guess_lower = guess.lower()
         word_list = ['orange', 'mango', 'banana', 'pear', 'tangerine']
         if guess in guess:
            print ("Good guess! {guess} is in the word.")
         else:
            print ("Sorry, {guess} is not in the word. Try again.")
        
    def ask_for_input (self,):
         while True:
            guess = input('guess a letter: ')
            if len(guess) != 1 or guess not in "abcdefghijklmnopqrstuvwxyz":
               print ("Invalid letter. Please, enter a single alphabetical character.")  
            elif guess in self.list_of_guesses :
                print ("You already tried that letter!")
            else:
                self.check_guess(guess)
word_list = ['orange', 'mango', 'banana', 'pear', 'tangerine']
tmp = HangMan(word_list)
print (tmp.ask_for_input())      
      



