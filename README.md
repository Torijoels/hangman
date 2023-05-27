# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

Milestone 1 
Setting up the environment
---
Milestone 2
The preliminary game logic for the overall project was established here. The main objective was to introduce control flows such as if else to help check user's input. The file milestone_2.py was created which contained the code for this milestone and  it contained random list called word_list wherein random choice of words can be selected at intervals. 


> Snapshot of Milestone 2

![](images/Screenshot%202023-01-21%20at%2010.25.45.png)


You should use an if statement to check if the letter entered by the user is in the word. Remember that the input should be stored in a variable called "guess" and the randomly picked word should be stored in a variable called "word". You can use the "in" operator to check if a character is in a string. If you think you have done it correctly, remember to use the right indentation for the if statement and just a single space between the "if" keyword and the condition

Check whether the letter guessed by the user is in the secret word that was randomly chosen by the computer. For example, if the user guesses the letter "a" and the secret word is "apple", then your code should check if "a" is in "apple".

Step 1. Create an if statement that checks if the guess is in the word.

Step 2. In the body of the if statement, print a message saying "Good guess! {guess} is in the word.". Obviously, format the string to show the actual guess instead of {guess}.

Step 3. Create an else block that prints a message saying "Sorry, {guess} is not in the word. Try again." This block of code will run if the guess is not in the word.



Milestone 3
To adequately capture the code in milestone 2, I created and defined functions called 'check_guess' and 'ask_for_input'.
These fucntions would check if the selected letter is in the word and the ask for input functions would iteratively check if the input is a valid guess.


Milestone 4
This stage captures the project in a Class called 'Hangman'. The class was initiatlised with the word_list and num_lives arguments.
The word_list depicts the entire words that can be guessed whilst the num_lives represents the number of times the player can repeat the game before reaching the end of the game.

Two methods 'check_guess' and 'ask_for_input' will allow the player confirm their guesses and validate that the letter guessed are in the secret 'word'.


Conclusions
Maybe write a conclusion to the project, what you understood about it and also how you would improve it or take it further.

Read through your documentation, do you understand everything you've written? Is everything clear and cohesive?? 


