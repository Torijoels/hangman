
import random
def check_guess ():
    guess = input ('Enter a single letter')
    guess.lower()
    word_list = ['Orange', 'Mango', 'Banana', 'Pear', 'Tangerine']
    import random
    random.choice (word_list)
    word = random.choice (word_list)
    if guess in word:
       print ("Good guess! {} is in the word.".format(guess))
    else:
       print ("Sorry, {} is not in the word. Try again.".format(guess))
# %%

def ask_for_input ():
      while True:
         guess = input('guess a letter: ')
         if len(guess) == 1 :
            print ("Good guess!")
         break
         print ("Invalid letter. Please, enter a single alphabetical character.")  
      check_guess ('c') 

# %%
ask_for_input()

#%%
class HangMan:
    def __init__(self, word_list, num_lives=5):

        self.word = random.choice (word_list)
        self.word_guessed = []
        self.num_letters = len(set())
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []


