import random
#%%
class HangMan:
    def __init__(self, word_list, num_lives=5):

        self.word = random.choice (word_list)
        self.word_guessed = []
        self.num_letters = len(set())
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []
        def check_guess (guess):
            guess.lower()
            word_list = ['Orange', 'Mango', 'Banana', 'Pear', 'Tangerine']
            random.choice (word_list)
            word = random.choice (word_list)
            if guess in word:
                print ("Good guess! {} is in the word.".format(guess))
            else:
                print ("Sorry, {} is not in the word. Try again.".format(guess))
        
        def ask_for_input ():
            while True:
              guess = input('guess a letter: ')
              if len(guess) != 1 :
                print ("Invalid letter. Please, enter a single alphabetical character.")  
              elif guess in self.list_of_guesses :
                print ("You already tried that letter!")
              else:
                check_guess (guess)
                guess = self.list_of_guesses
        #%%
        ask_for_input ()


# %%
