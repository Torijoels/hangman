import random
word_list = ['Orange', 'Mango', 'Banana', 'Pear', 'Tangerine']

#%%
class HangMan:
    def __init__(self, word_list, num_lives=5):

        self.word = random.choice (word_list)
        self.word_guessed = ['', '', '', '', '']
        self.num_letters = len(set())
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []
        def check_guess (guess):
            guess = input('guess a letter: ')
            guess.lower()
            word_list = ['Orange', 'Mango', 'Banana', 'Pear', 'Tangerine']
            random.choice (word_list)
            word = random.choice (word_list)
            if guess in word:
                print ("Good guess! {} is in the word.".format(guess))
                for letter in word:
                   if letter in self.word_guessed:
                       print(f"letter", end="")
                   else:
                       print (f"_", end="")
                self.num_letters -= 1
            else:
                print ("Sorry, {letter} is not in the word. Try again.")
                self.num_lives -= 1
                print ("You have {num_lives} lives left.")

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
def play_game (word_List):
    num_lives = 5
    num_letters = []
    game = HangMan (word_list, num_lives)
    while True: 
     if num_lives == 0 :
        print ("You lost")
     elif num_letters > 0 :
        ask_input = HangMan ()
        print (ask_input.ask_for_input())
     else:
        print ("Congratulations. You won the game!")
    return 
# %%
play_game (word_list)

# %%
