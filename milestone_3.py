# %%
#Task1 Continously run code until user inputs right letter

# %%
#Task 2 check whether the guess is in the word

# %%

#Task 3 create the function to run tests
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



# %%
#Task 3 create the function to run tests

 
