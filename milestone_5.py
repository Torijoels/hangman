import random


class HangMan:
    def __init__(self, word_list, num_lives=5):
        self.word = random.choice (word_list)
        self.word_guessed = []
        self.num_letters = len(set(self.word_guessed))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []  

    def check_guess (self):
         guess = input('guess one letter: ')
         guess_lower = guess.lower()
         word_list = ['orange', 'mango', 'banana', 'pear', 'tangerine']
         if guess_lower in guess:
            print ("Good guess! {guess} is in the word.")
         else:
            print ("Sorry, {guess} is not in the word. Try again.")
        
    def ask_for_input (self):
         while True:
            guess = input('guess one letter: ')
            if len(guess) != 1 or not guess.isalpha():
               print ("Invalid letter. Please, enter a single alphabetical character.")  
            elif guess in self.list_of_guesses :
                print ("You already tried that letter!")
            else:
                self.check_guess()
word_list = ['orange', 'mango', 'banana', 'pear', 'tangerine']
     
def play_game (word_List):
     num_lives = 5
     game = HangMan (word_list, num_lives)
     game.num_letters
     while True: 
       if num_lives == 0 :
        print ("You lost")
       elif game.num_letters > 0 :
          game.ask_for_input ()
       else :
        print ("Congratulations. You won the game!")
       break

play_game (word_list)



# %%
