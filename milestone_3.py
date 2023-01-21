# %%
#Task1 Continously run code until user inputs right letter
while True:
     guess = input('guess a letter: ')
     if len(guess) == 1 :
        print ("Good guess!")
        break
     print ("Invalid letter. Please, enter a single alphabetical character.")  
# %%
