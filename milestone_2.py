import random
#Task 1  and 2
word_list = ['Orange', 'Mango', 'Banana', 'Pear', 'Tangerine']
random.choice (word_list)
word = random.choice (word_list)
print (word)

#Task 3
#Ask the user for an input
# %%
guess = input ('Enter a single letter')
print(guess)

# Task 4
# Checking that the user entered a valid input 
# %%
guess = input ('Enter a single letter')
print(guess)
if len(guess) == 1 : 
    print ("Good guess!")
elif guess.isalpha():
    print ("Good guess!")
else:
    print ("Oops! That is not a valid input." )
# %%
