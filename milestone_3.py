# %%
#Task1 Continously run code until user inputs right letter
while True:
     guess = input('guess a letter: ')
     if len(guess) == 1 :
        print ("Good guess!")
        break
     print ("Invalid letter. Please, enter a single alphabetical character.")  
# %%
#Task 2 check whether the guess is in the word
word_list = ['Orange', 'Mango', 'Banana', 'Pear', 'Tangerine']
import random
random.choice (word_list)
word = random.choice (word_list)
guess = input ('Enter a single letter')
if guess in word:
    print ("Good guess! {} is in the word.".format(guess))
else:
    print ("Sorry, {} is not in the word. Try again.".format(guess))
# %%
