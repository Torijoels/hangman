# %%
#Task1 Interatively check if the input is a valid guess
guess = input('guess a letter')
while len(guess) == 1:
      print ("Good guess!")
      break
else:
    print ("Invalid letter. Please, enter a single alphabetical character.")


